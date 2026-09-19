from src.business_assistant import answer_business_question

question = "How many repeat customers do we have?"

sql, columns, results, insight, chart = answer_business_question(question)

print("Business Question:")
print(question)

print("\nGenerated SQL:")
print(sql)

print("\nDatabase Result:")
print(results)

print("\nBusiness Insight:")
print(insight)

if chart:
    chart.write_html("category_sales_ai.html")
    print("\nChart created successfully!")