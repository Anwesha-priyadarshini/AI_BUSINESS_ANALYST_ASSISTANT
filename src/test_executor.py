from src.sql_executor import execute_sql

sql = 'SELECT SUM("Amount") FROM order_details;'

results = execute_sql(sql)

print("Query results:")
print(results)