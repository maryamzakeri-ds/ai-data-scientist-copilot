import requests

API_URL = 'http://127.0.0.1:8000'

def ask_chat(question):
    response = requests.post(
        f'{API_URL}/chat',
        json={'question': question}
    )
    response.raise_for_status()
    return response.json()