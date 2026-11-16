import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    base_url='https://openrouter.ai/api/v1',
    api_key=os.getenv('OPENROUTER_API_KEY')
)

def ask_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model='openai/gpt-oss-20b',
        messages=[
            {
                'role': 'system',
                'content': """
                    You are an AI Data Scientist Copilot.
                    Help users analyze datasets and answer their questions.
                """
            },
            {
                'role': 'user',
                'content': prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content

def build_prompt(question, metadata):
    prompt = f"""
        You are working with the following dataset:
        Dataset name: {metadata['filename']}
        Dataset table: {metadata['table_name']}
        Dataset profile: {metadata['profile_json']}
        Cleaning Operations: {metadata['cleaning_report']}

        User question: {question}

        Instructions:
        1. If the question can be answered using ONLY the dataset metadata, return:
        {{
            'needs_sql': false,
            'answer': 'your answer'
        }}

        2. If the question requires analyzing the dataset, return:
        {{
            'needs_sql': true,
            'sql': 'your PostgreSQL query'
        }}

        Rules:
        - Return ONLY valid JSON.
        - Do not use markdown.
        - Do not wrap the JSON in ``` blocks.
        - If generating SQL, genearte ONLY a PostgreSQL SELECT query.
        - Never generate INSERT, UPDATE, DELETE, DROP, ALTER, CREATE, TRUNCATE or any statement that modifies the dataset.
    """
    return prompt