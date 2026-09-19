import plotly.express as px


def create_category_sales_chart(results):
    categories = []
    sales = []

    for category, category_sales in results:
        categories.append(category)
        sales.append(category_sales)

    fig = px.bar(
        x=categories,
        y=sales,
        labels={
            "x": "Category",
            "y": "Sales"
        },
        title="Sales by Category"
    )

    return fig