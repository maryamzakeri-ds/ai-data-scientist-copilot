# AI Data Scientist Copilot

## Project Overview

Building an AI-powered Data Science assistant that helps business users explore datasets, answer analytical questions, generate insights, and automate repetitive data analysis tasks using LLMs and machine learning tools.

## Problem Statement

A retail company has thousands of daily transactions. Business managers need quick answers about sales performance, customer behavior, and revenue trends, but data analysis requires technical expertise.

## Target Users

Primary user: Business analysts and managers who need fast insights without writing SQL/Python.

## Main Features

Data Understanding
- Automatically detect data types
- Generate dataset summary
- Identify missing values and anomalies

Natural Language Analytics
User:
Why did revenue decrease in March?

System:
- Generates SQL
- Runs analysis
- Creates visualization
- Explains findings

Visualization Generation
- Recommend suitable charts
- Generate plots

Machine Learning Assistant
- Train baseline models
- Compare results
- Explain metrics

## Tech Stack

Frontend:
Streamlit

Backend:
FastAPI

LLM:
Open-source local models via Ollama

RAG:
ChromaDB + Embedding models

Database:
PostgreSQL

Data Processing:
Pandas

ML:
Scikit-learn

Containerization:
Docker

CI/CD:
Jenkins

BI:
Metabase

## Success Metrics

Technical Metrics
- Accuracy of generated analytical answers
- Successful SQL generation rate
- Response time

User Metrics
- User can answer business questions without coding
- Reduction in time required for routine analysis

## MVP Scope

MVP Version 1
Input:
CSV file

System can:
1. Analyze dataset automatically:
   - columns
   - types
   - missing values
   - statistics
2. Answer questions:
   Example:
   What are the top-selling products?
3. Generate:
   - SQL/Pandas operation
   - Visualization
   - Explanation

## Future Improvements

RAG over company documents
ML model training assistant
Automated reporting
Multi-agent architecture
Fine-tuning domain-specific models
Cloud deployment


