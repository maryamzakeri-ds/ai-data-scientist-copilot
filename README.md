# AI Data Scientist Copilot 🤖📊

An AI-powered assistant for data analysis that helps users explore, understand, and interact with their datasets using natural language.

The goal of this project is to build a data science copilot that can take a dataset, automatically analyze its structure, store metadata, and answer analytical questions by combining LLM capabilities with data processing and databases.

> 🚧 This project is under active development.

---

## ✨ Features (Current)

### Dataset Upload & Processing
- Upload CSV datasets
- Automatically profile datasets
- Detect:
  - Number of rows and columns
  - Missing values
  - Data types
  - Duplicate rows
  - Column categories (numeric, categorical, boolean, identifier)

### Data Cleaning Pipeline
- Normalize column names
- Trim text values
- Standardize missing values
- Convert numeric columns
- Remove duplicate rows
- Save processed datasets separately

### Metadata Management
- Store dataset information in PostgreSQL
- Keep metadata including:
  - Dataset name
  - Database table name
  - Dataset profile
  - Cleaning report
  - Upload timestamp
  - Processing status

### LLM Integration
The assistant uses dataset metadata as context to answer questions about uploaded datasets.

The LLM can decide whether:
- The question can be answered from metadata
- A SQL query is required for deeper analysis

---

## 🏗️ Architecture

Current workflow:

```
User
 |
 | Upload CSV
 ↓
FastAPI Backend
 |
 ↓
Data Profiling
 |
 ↓
Data Cleaning
 |
 ↓
PostgreSQL
 |
 ↓
Metadata Extraction
 |
 ↓
LLM Assistant
```

Future workflow:

```
User Question
      |
      ↓
      LLM
      |
      ↓
SQL Generation
      |
      ↓
SQL Validation
      |
      ↓
PostgreSQL Query Execution
      |
      ↓
Result Explanation
```

---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- PostgreSQL

### Data Processing
- Pandas
- NumPy

### AI / LLM
- OpenAI-compatible LLM APIs
- Prompt engineering
- Text-to-SQL (in development)

### Frontend (planned)
- Dash
- Plotly

---

## 🚀 Roadmap

- [x] CSV upload API
- [x] Automated dataset profiling
- [x] Data cleaning pipeline
- [x] PostgreSQL dataset storage
- [x] Dataset metadata storage
- [x] LLM connection
- [ ] Natural language question answering
- [ ] Text-to-SQL generation
- [ ] SQL validation and safety layer
- [ ] Automatic visualization generation
- [ ] Streamlit user interface
- [ ] ML model training and evaluation assistant

---

## 🎯 Project Goal

The long-term goal is to create an AI assistant that enables users to interact with their data naturally, reducing the gap between raw datasets and actionable insights.

Instead of writing code for every analysis step, users can ask questions in natural language and receive data-driven answers.

---

## 👩‍💻 Author

Maryam Zakeri

Computer Engineering | Data Science & AI

GitHub:
https://github.com/maryamzakeri-ds