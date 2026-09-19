from src.sql_generator import generate_sql

question = "What is the total sales?"

sql = generate_sql(question)

print("Generated SQL:")
print(sql)