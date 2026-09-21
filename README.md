# 🤖 AI Business Analyst Assistant

An AI-powered business analytics assistant that allows users to ask business questions in natural language and receive data-driven answers from a structured business database.

The application converts natural-language questions into SQL queries, validates the generated SQL, executes the query against a SQLite database, and uses AI to explain the results in simple business language.

---

## 📸 Dashboard Preview

![AI Business Analyst Assistant Dashboard](dashboard.png)

---

## 📌 Business Problem

Business analysts often spend significant time answering repetitive questions such as:

- Which category generated the highest profit?
- Which month had the highest sales?
- Which state has the highest sales?
- Which category has the lowest profit margin?
- Where are the major losses occurring?

This project demonstrates an AI-assisted analytics workflow that helps answer these questions more efficiently.

---

## 💡 Solution

The **AI Business Analyst Assistant** allows a business user to enter a question in natural language.

The system then:

1. Understands the business question using an LLM.
2. Generates a SQLite SQL query.
3. Validates the SQL query for safety.
4. Executes the query against the business database.
5. Retrieves the relevant results.
6. Generates a concise business insight.
7. Displays the result in a Streamlit dashboard.
8. Creates a visualization when appropriate.

---

## 🏗️ Architecture

```text
Business User
      ↓
Natural-Language Question
      ↓
AI Business Analyst Assistant
      ↓
AI-Generated SQL
      ↓
SQL Validation
      ↓
SQLite Database
      ↓
Query Results
      ↓
AI Business Insight
      ↓
Streamlit Dashboard
      ↓
Visualization
```

---

## 🛠️ Technology Stack

- **Python**
- **SQLite**
- **SQL**
- **Pandas**
- **Plotly**
- **Streamlit**
- **OpenAI API**
- **python-dotenv**

---

## 📊 Dataset

The project uses an Indian e-commerce sales dataset containing:

- Orders
- Customers
- States and cities
- Sales amounts
- Profit
- Quantity
- Categories
- Sub-categories
- Sales targets

The dataset is used to demonstrate business analysis and natural-language-to-SQL workflows.

---

## 📈 Key Business Insights

- **Electronics** generated the highest sales at approximately ₹165K.
- **Clothing** generated the highest total profit at approximately ₹11.2K.
- **Furniture** had the lowest profit margin at approximately 1.81%.
- Within Furniture, **Tables** generated approximately ₹22.6K in sales but recorded a loss of approximately ₹4.0K.
- **Tamil Nadu and Madhya Pradesh** together accounted for approximately 90.7% of the total loss from Furniture Tables.

---

## 💬 Example Business Questions

The assistant can answer questions such as:

```text
Which category has the highest profit?

Which month had the highest sales?

Which state generated the highest sales?

Which category has the lowest profit margin?

Which Furniture sub-category has the lowest profit?

Which states have losses in Furniture Tables?

What are the sales and profit of Furniture Tables in Tamil Nadu and Madhya Pradesh?
```

---

## 🔐 SQL Safety

The application includes SQL validation before executing AI-generated queries.

The validator:

- Allows only `SELECT` statements and read-only `WITH` queries.
- Blocks multiple SQL statements.
- Blocks database-changing operations such as:
  - `INSERT`
  - `UPDATE`
  - `DELETE`
  - `DROP`
  - `ALTER`
  - `CREATE`
  - `REPLACE`
  - `TRUNCATE`
  - `ATTACH`
  - `DETACH`
  - `PRAGMA`

This provides an additional safety layer between AI-generated SQL and the database.

---

## 📂 Project Structure

```text
AI_BUSINESS_ANALYST_ASSISTANT
│
├── data
│   ├── List of Orders.csv
│   ├── Order Details.csv
│   └── Sales target.csv
│
├── database
│   └── business_data.db
│
├── src
│   ├── analytics.py
│   ├── app.py
│   ├── business_assistant.py
│   ├── category_analysis.py
│   ├── config.py
│   ├── database_setup.py
│   ├── insight_generator.py
│   ├── load_data.py
│   ├── openai_client.py
│   ├── schema.py
│   ├── sql_executor.py
│   ├── sql_generator.py
│   ├── sql_validator.py
│   ├── test_ai.py
│   ├── test_business_assistant.py
│   └── visualizations.py
│
├── dashboard.png
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Anwesha-priyadarshini/AI_BUSINESS_ANALYST_ASSISTANT.git
```

### 2. Open the project

```bash
cd AI_BUSINESS_ANALYST_ASSISTANT
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the OpenAI API key

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
```

The `.env` file is excluded from Git using `.gitignore`.

### 7. Create the database

```bash
python src/database_setup.py
```

### 8. Load the dataset

```bash
python src/load_data.py
```

### 9. Start the Streamlit application

```bash
streamlit run src/app.py
```

The application will open in the browser.

---

## 🔄 Application Workflow

```text
Business Question
        ↓
Natural Language Understanding
        ↓
AI-Generated SQL
        ↓
SQL Validation
        ↓
SQLite Query Execution
        ↓
Database Results
        ↓
AI Business Insight
        ↓
Visualization
```

---

## ⚠️ Limitations

- The assistant depends on the quality of the generated SQL.
- Complex business questions may require additional SQL-generation rules.
- The current visualization logic supports selected question patterns rather than automatically visualizing every query.
- The dataset is a sample e-commerce dataset and may not represent a real production business environment.
- AI-generated insights are based only on the data returned by the executed SQL query.

---

## 🚀 Future Improvements

- Add more advanced natural-language-to-SQL capabilities.
- Add automatic chart selection based on query results.
- Support more business KPIs and analytical questions.
- Add query-result validation and anomaly detection.
- Add conversation history.
- Add user authentication.
- Add support for larger production databases.
- Integrate LangChain or other orchestration frameworks where useful.
- Add deployment to a cloud platform.

---

## 👩‍💻 Author

**Anwesha Priyadarshini**

Computer Science & Engineering Graduate

GitHub:
https://github.com/Anwesha-priyadarshini

---

## ⭐ Project Goal

The goal of this project is to demonstrate how AI, SQL, Python, and business analytics can be combined to create an interactive analytics assistant that helps users move from natural-language business questions to data-driven insights.