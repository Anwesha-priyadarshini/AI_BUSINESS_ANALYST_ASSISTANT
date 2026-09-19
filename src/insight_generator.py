from src.openai_client import ask_ai


def generate_business_insight(question, sql, results):
    prompt = f"""
You are a business analyst.

Business question:
{question}

SQL query used:
{sql}

Database result:
{results}

Explain the result in simple business language.

Rules:
- Give the direct answer first.
- Use the actual numbers from the database result.
- The dataset uses Indian currency. Use ₹ when referring to monetary amounts.
- Do not invent information.
- Keep the answer concise.
"""

    return ask_ai(prompt)