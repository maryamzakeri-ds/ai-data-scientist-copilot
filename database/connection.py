from sqlalchemy import create_engine

DATABASE_URL = 'postgresql+psycopg2://postgres:Quality6285@localhost:5432/ai_copilot'

engine = create_engine(DATABASE_URL)
