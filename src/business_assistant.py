from src.sql_generator import generate_sql
from src.sql_executor import execute_sql
from src.insight_generator import generate_business_insight
from src.visualizations import create_category_sales_chart


def answer_business_question(question):
    sql = generate_sql(question)

    columns, results = execute_sql(sql)

    insight = generate_business_insight(
        question,
        sql,
        results
    )

    chart = None

    if "category" in question.lower() and "sales" in question.lower():
        chart = create_category_sales_chart(results)

    return sql, columns, results, insight, chart