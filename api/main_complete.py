from fastapi import FastAPI, UploadFile, File
import pandas as pd
import shutil
from pathlib import Path
from app.services.profiler import profile_dataset
from app.services.cleaner import clean_dataset
import re
from database.connection import engine
from app.services.llm_service import ask_llm, build_prompt
from pydantic import BaseModel
from contextlib import asynccontextmanager
from database.metadata import create_metadata_table, save_dataset_metadata, get_latest_metadata, get_datasets


BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = BASE_DIR / 'data' / 'raw'
RAW_DATA_PATH.mkdir(parents=True, exist_ok=True)

PROCESSED_DATA_PATH = BASE_DIR / 'data' / 'processed'
PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_metadata_table()
    yield


app = FastAPI(
    title="AI Data Scientist Copilot",
    lifespan=lifespan
)

@app.get('/')
def home():
    return {
        'message' : 'AI Data Scientist is running'
    }

@app.post('/upload')
def upload_file(file: UploadFile = File(...)):
    file_path = RAW_DATA_PATH / file.filename

    with open(file_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    df = pd.read_csv(file_path)

    profile = profile_dataset(df)

    cleaned_df, cleaning_report = clean_dataset(df)

    cleaned_df.to_csv(PROCESSED_DATA_PATH/f'cleaned_{file.filename}', index=False)

    table_name = Path(file.filename).stem.lower()
    table_name = re.sub(r'[^a-z0-9]+', '_', table_name)
    table_name = table_name.strip('_')

    cleaned_df.to_sql(
        table_name,
        engine,
        if_exists='replace',
        index=False
    )

    save_dataset_metadata(file.filename, table_name, profile, cleaning_report)

    return {
        'filename': file.filename,
        'profile': profile,
        'cleaning_report': cleaning_report
    }


class ChatRequest(BaseModel):
    table_name: str
    question: str

@app.post('/chat')
def chat(request: ChatRequest):
    metadata = get_latest_metadata(request.table_name)
    prompt = build_prompt(request.question, metadata)
    answer = ask_llm(prompt)

    if answer['needs_sql']:
        pass
    else:
        return {
            'question': request.question,
            'answer': answer
        }


@app.get('/datasets')
def datasets():
    return get_datasets()
