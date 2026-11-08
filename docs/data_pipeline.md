# Data Pipeline

## 1. Data Ingestion

CSV or excel file uploaded by user

## 2. Data Validation

- Checking missing values
- Checking for empty strings
- Checking for unusual data entries based on business rules such as negative numbers
- Checking for duplicates
- Checking Data Types

## 3. Data Cleaning

- Imputing missing values based on data types

## 4. Data Storage

- Raw data is received by user and stores in data/raw
- After cleaning and performing other process on data, it will be stored in data/processed.
- After processing the data needed for analytics is stored in the database.

## 5. Data Flow Diagram

User Upload
      |
Validation
      |
Raw Storage
      |
Cleaning
      |
Processed Storage
      |
Load into PostgreSQL
      |
Analytics Engine
      |
LLM Agent
      |
User Response

