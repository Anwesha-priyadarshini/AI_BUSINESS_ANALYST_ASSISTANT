import sqlite3

connection = sqlite3.connect("database/business_data.db")

print("Database created successfully!")

connection.close()