import sqlite3

connection = sqlite3.connect("database/business_data.db")

query = """
SELECT
    strftime(
        '%Y-%m',
        substr(orders."Order Date", 7, 4) || '-' ||
        substr(orders."Order Date", 4, 2) || '-' ||
        substr(orders."Order Date", 1, 2)
    ) AS Month,
    ROUND(SUM(order_details.Amount), 2) AS Sales
FROM orders
JOIN order_details
    ON orders."Order ID" = order_details."Order ID"
GROUP BY Month
ORDER BY Month;
"""

rows = connection.execute(query).fetchall()

print("Month | Sales")
print(*rows, sep="\n")

connection.close()