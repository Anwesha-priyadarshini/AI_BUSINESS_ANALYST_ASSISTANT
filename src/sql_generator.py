from src.openai_client import ask_ai
from src.schema import DATABASE_SCHEMA


def generate_sql(question):

    prompt = f"""
You are a SQL analyst.

Here is the database schema:

{DATABASE_SCHEMA}

Convert the following business question into a SQLite SQL query.

Business question:
{question}

Return ONLY the SQL query.
Do not include explanations.

SQL rules:
- Generate valid SQLite SQL.
- Only use SELECT statements or read-only WITH queries.
- Avoid complex UNION queries unless necessary.
- When using UNION or UNION ALL, only ORDER BY columns that are present in the final result.
- Do not use an ORDER BY expression that is not a selected column.
"""

    sql = ask_ai(prompt)

    if not sql:
        raise ValueError("AI did not return a SQL query.")

    print("\nAI Generated SQL:")
    print(sql)

    return sql