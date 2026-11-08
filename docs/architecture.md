# System Architecture

## Overview

The system follows a modular architecture where Streamlit handles user interaction, FastAPI manages communication between services, the Data Engine performs analytical tasks, and the LLM Agent orchestrates tools and generates explanations.

## Components

### 1. Frontend

Role:

- Upload CSV files
- Display dataset summaries
- Provide chat interface
- Visualize generated charts
- Display analytical results

Technology: Streamlit

### 2. Backend

Role: 
- Receiving CSV File
- Managing queries
- Interface for Components
- Sending the answers to UI
- Request validation
- Session management
- API endpoints

Technology: FastAPI

### 3. Data Engine

Role: 
Role:

- Data profiling
- Data cleaning
- Statistical analysis
- SQL query execution
- Visualization generation

Technology: Pandas, SQL

### 4. RAG System

Role:

- Data Dictionary
- Company Documentation
- Previous Reports

Technology: ChromaDB + Embedding models

Process:
- Documents are converted into embeddings
- Embeddings are stored in vector database
- Relevant context is retrieved for LLM

### 5. LLM Agent

Role:

- Understand user intent
- Select appropriate tools
- Generate tool calls
- Combine results
- Generate natural language explanations

Technology: Open-source local models via Ollama

### 6. Database

Role:

- Store structured datasets
- Store metadata
- Store user sessions
- Store analysis history
- Support SQL-based analysis

Technology: PostgreSQL

## Data Flow

1. User uploads CSV through Streamlit

2. FastAPI receives file

3. Data Engine performs profiling

4. Data is stored in PostgreSQL

5. Metadata/Data Dictionary is created

6. User asks a question

7. LLM Agent analyzes intent

8. Agent selects tools

9. Data Engine executes analysis

10. Results return to Agent

11. LLM generates explanation

12. Streamlit displays answer and visualization
