import sqlite3


def run_query(query):
    connection = sqlite3.connect("database/business_data.db")
    rows = connection.execute(query).fetchall()
    connection.close()
    return rows


def get_total_sales():
    query = """
    SELECT ROUND(SUM(Amount), 2)
    FROM order_details;
    """

    return run_query(query)[0][0]


def get_total_profit():
    query = """
    SELECT ROUND(SUM(Profit), 2)
    FROM order_details;
    """

    return run_query(query)[0][0]


def get_profit_margin():
    query = """
    SELECT ROUND(
        SUM(Profit) * 100.0 / SUM(Amount),
        2
    )
    FROM order_details;
    """

    return run_query(query)[0][0]


def get_category_analysis():
    query = """
    SELECT
        Category,
        ROUND(SUM(Amount), 2) AS Sales,
        ROUND(SUM(Profit), 2) AS Profit,
        ROUND(SUM(Profit) * 100.0 / SUM(Amount), 2) AS Profit_Margin
    FROM order_details
    GROUP BY Category
    ORDER BY Sales DESC;
    """

    return run_query(query)


def get_monthly_sales():
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

    return run_query(query)

def get_customer_analysis():
    query = """
    SELECT
        COUNT(DISTINCT CustomerName) AS Total_Customers,
        COUNT(
            CASE
                WHEN Order_Count > 1 THEN 1
            END
        ) AS Repeat_Customers
    FROM (
        SELECT
            CustomerName,
            COUNT(*) AS Order_Count
        FROM orders
        GROUP BY CustomerName
    );
    """

    return run_query(query)