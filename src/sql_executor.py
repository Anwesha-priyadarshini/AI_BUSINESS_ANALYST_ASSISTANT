import sqlite3

from src.sql_validator import validate_sql


def execute_sql(sql):
    if not validate_sql(sql):
        raise ValueError("Unsafe SQL query rejected.")

    connection = sqlite3.connect("database/business_data.db")

    try:
        cursor = connection.execute(sql)

        results = cursor.fetchall()

        columns = [column[0] for column in cursor.description]

        return columns, results

    finally:
        connection.close()