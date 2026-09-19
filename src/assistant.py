from src.analytics import (
    get_total_sales,
    get_total_profit,
    get_profit_margin,
    get_category_analysis,
    get_monthly_sales,
    get_customer_analysis
)

from src.visualizations import create_category_sales_chart


def answer_question(question):
    question = question.lower()

    if "total sales" in question:
        return get_total_sales()

    elif "total profit" in question:
        return get_total_profit()

    elif "profit margin" in question:
        return get_profit_margin()

    elif "category" in question:
        results = get_category_analysis()

        answer = "Category Performance:\n"

        for category, sales, profit, margin in results:
            answer += (
                f"{category}: Sales ₹{sales:,.0f}, "
                f"Profit ₹{profit:,.0f}, "
                f"Profit Margin {margin}%\n"
            )

        chart = create_category_sales_chart(results)
        chart.write_html("category_sales.html")

        return answer

    elif "highest sales" in question or "best month" in question:
       results = get_monthly_sales()

       highest_month, highest_sales = max(
        results,
        key=lambda x: x[1]
       )

       return (
        f"Highest Sales Month: {highest_month}\n"
        f"Sales: ₹{highest_sales:,.0f}"
       )

    elif "month" in question or "monthly" in question:
       results = get_monthly_sales()

       answer = "Monthly Sales:\n"

       for month, sales in results:
        answer += f"{month}: Sales ₹{sales:,.0f}\n"

       return answer

    elif "customer" in question or "repeat" in question:
        results = get_customer_analysis()

        total_customers, repeat_customers = results[0]
        one_time_customers = total_customers - repeat_customers
        repeat_rate = repeat_customers * 100 / total_customers

        answer = (
           f"Customer Analysis:\n"
           f"Total Customers: {total_customers}\n"
           f"Repeat Customers: {repeat_customers}\n"
           f"One-Time Customers: {one_time_customers}\n"
           f"Repeat Customer Rate: {repeat_rate:.2f}%"
        )

        return answer
    else:
        return "I don't understand this question yet."