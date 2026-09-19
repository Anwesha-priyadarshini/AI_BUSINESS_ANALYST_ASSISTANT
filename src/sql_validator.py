import re


def validate_sql(sql):
    sql = sql.strip()

    # SQL must not be empty
    if not sql:
        return False

    # Only allow SELECT statements or read-only WITH queries
    if not re.match(r"^(SELECT|WITH)\b", sql, re.IGNORECASE):
        return False

    # Remove SQL comments before checking for dangerous commands
    sql_without_comments = re.sub(
        r"--.*?$|/\*.*?\*/",
        "",
        sql,
        flags=re.MULTILINE | re.DOTALL
    )

    # Block multiple statements
    statements = [
        statement.strip()
        for statement in sql_without_comments.split(";")
        if statement.strip()
    ]

    if len(statements) != 1:
        return False

    # Block database-changing operations
    forbidden_patterns = [
        r"\bINSERT\b",
        r"\bUPDATE\b",
        r"\bDELETE\b",
        r"\bDROP\b",
        r"\bALTER\b",
        r"\bCREATE\b",
        r"\bREPLACE\b",
        r"\bTRUNCATE\b",
        r"\bATTACH\b",
        r"\bDETACH\b",
        r"\bPRAGMA\b"
    ]

    for pattern in forbidden_patterns:
        if re.search(pattern, sql_without_comments, re.IGNORECASE):
            return False

    return True

