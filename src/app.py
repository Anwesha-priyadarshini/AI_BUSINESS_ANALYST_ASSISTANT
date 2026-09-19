import sys
from pathlib import Path

import pandas as pd
import streamlit as st


# Project root
project_root = Path(__file__).resolve().parent.parent

if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))


from src.business_assistant import answer_business_question
from src.analytics import (
    get_total_sales,
    get_total_profit,
    get_profit_margin
)


# Page configuration
st.set_page_config(
    page_title="AI Business Analyst Assistant",
    page_icon="📊",
    layout="wide"
)


# Sidebar
with st.sidebar:

    st.header("About the Assistant")

    st.write(
        "This AI-powered analytics assistant converts "
        "natural-language business questions into SQL queries, "
        "analyzes database results, and generates business insights."
    )

    st.subheader("Technology")

    st.write(
        "Python • SQLite • SQL • Pandas • Plotly • OpenAI"
    )

    st.subheader("Capabilities")

    st.markdown(
    """
    ✓ Natural-language questions  
    ✓ AI-generated SQL  
    ✓ Database analysis  
    ✓ Business insights  
    ✓ Interactive visualizations
    """
)

    st.subheader("Dataset")

    st.write(
        "Indian e-commerce sales dataset with "
        "orders, customers, products, sales, profit, "
        "categories, sub-categories, and sales targets."
    )

    st.subheader("How It Works")

    st.write(
        "Business Question → AI → SQL → Database → "
        "Analysis → Insight"
    )


# Main page
st.title("📊 AI Business Analyst Assistant")

st.subheader(
    "Ask business questions and get AI-powered, data-driven insights."
)

st.write(
    "Ask a business question and get data-driven insights from the database."
)
# KPI cards
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Sales",
        f"₹{get_total_sales():,.0f}"
    )

with col2:
    st.metric(
        "Total Profit",
        f"₹{get_total_profit():,.0f}"
    )

with col3:
    st.metric(
        "Profit Margin",
        f"{get_profit_margin():.2f}%"
    )

# Business question input
question = st.text_input(
    "Enter your business question:",
    placeholder="Example: Which category has the highest profit?"
)


# Example questions
st.caption("Try questions like:")

st.markdown(
    """
    - Which category has the highest profit?
    - Which state generated the highest sales?
    - Which month had the highest sales?
    - Which category has the lowest profit margin?
    """
)


# Analyze button
if st.button("Analyze"):

    if question:

        try:

            with st.spinner("Analyzing your question..."):

                sql, columns, results, insight, chart = (
                    answer_business_question(question)
                )

        except Exception as error:

            st.error(
                "Sorry, I couldn't analyze that question. "
                "Please try again or ask a simpler business question."
            )

            st.caption(
                f"Technical details: {error}"
            )

            st.stop()


        # Business insight
        st.subheader("Business Insight")

        st.write(insight)


        # Generated SQL
        st.subheader("Generated SQL")

        st.code(
            sql,
            language="sql"
        )


        # Database result
        st.subheader("Database Result")

        if results:

            # Check whether the database returned only empty values
            if all(
                value is None
                for row in results
                for value in row
            ):

                st.info(
                    "No matching data was found for this question."
                )

            else:

                result_df = pd.DataFrame(
                    results,
                    columns=columns
                )


                # Format numeric values as Indian currency
                for column in result_df.columns:

                    if result_df[column].dtype in [
                        "float64",
                        "int64"
                    ]:

                        result_df[column] = result_df[column].apply(
                            lambda x: f"₹{x:,.2f}"
                            if isinstance(x, (int, float))
                            else x
                        )


                st.dataframe(
                    result_df,
                    width="stretch",
                    hide_index=True
                )

        else:

            st.info(
                "No data was returned."
            )


        # Visualization
        if chart:

            st.subheader("Visualization")

            st.plotly_chart(
                chart,
                width="stretch"

            )


    else:

        st.warning(
            "Please enter a business question."
        )