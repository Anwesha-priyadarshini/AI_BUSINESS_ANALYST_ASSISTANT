import sqlite3
import pandas as pd

# Read CSV files
orders = pd.read_csv("data/List of Orders.csv")
order_details = pd.read_csv("data/Order Details.csv")
sales_targets = pd.read_csv("data/Sales target.csv")

# Connect to SQLite database
connection = sqlite3.connect("database/business_data.db")

# Load data into SQLite tables
orders.to_sql("orders", connection, if_exists="replace", index=False)
order_details.to_sql("order_details", connection, if_exists="replace", index=False)
sales_targets.to_sql("sales_targets", connection, if_exists="replace", index=False)

print("Data loaded successfully!")

# Check database tables
tables = connection.execute(
    "SELECT name FROM sqlite_master WHERE type='table'"
).fetchall()

print("Tables:", tables)

# Close connection
connection.close()