DATABASE_SCHEMA = """
Database: business_data.db

Table: orders
Columns:
- Order ID
- Order Date
- CustomerName
- State
- City

Important:
- orders."Order Date" is stored as text in DD-MM-YYYY format.
- When using SQLite date functions, convert it to YYYY-MM-DD first.

Table: order_details
Columns:
- Order ID
- Amount
- Profit
- Quantity
- Category
- Sub-Category

Table: sales_targets
Columns:
- Month of Order Date
- Category
- Target

Relationships:
- orders."Order ID" = order_details."Order ID"
"""