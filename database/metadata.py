from sqlalchemy import text
from database.connection import engine
import json

def create_metadata_table():
    query = """
        CREATE TABLE IF NOT EXISTS
        dataset_metadata (
            id SERIAL PRIMARY KEY,
            filename VARCHAR(255) NOT NULL,
            table_name VARCHAR(255) UNIQUE NOT NULL,
            profile_json JSONB,
            cleaning_report JSONB,
            uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            status VARCHAR(50)
        );

    """

    with engine.connect() as conn:
        conn.execute(text(query))
        conn.commit()


def save_dataset_metadata( filename, table_name, profile, cleaning_report):
    delete_query = """
        DELETE FROM dataset_metadata WHERE table_name = :table_name
    """
    insert_query = """
        INSERT INTO dataset_metadata
        (
            filename,
            table_name,
            profile_json,
            cleaning_report,
            status
        )
        VALUES
        (
            :filename,
            :table_name,
            :profile_json,
            :cleaning_report,
            :status
        )
    """

    with engine.connect() as conn:
        conn.execute(text(delete_query), {'table_name': table_name})
        conn.execute(
            text(insert_query), 
            {
                'filename': filename,
                'table_name': table_name,
                'profile_json': json.dumps(profile),
                'cleaning_report': json.dumps(cleaning_report),
                'status': 'success'
            }
        )
        conn.commit()


def get_latest_metadata(table_name):
    query = """
        SELECT * FROM dataset_metadata WHERE table_name = :table_name
    """

    with engine.connect() as conn:
        result = conn.execute(text(query), {'table_name': table_name}).mappings().first()

    return result


def get_datasets():
    query = """
        SELECT filename, table_name FROM dataset_metadata ORDER BY uploaded_at DESC
    """

    with engine.connect() as conn:
        result = conn.execute(text(query)).mappings().all()

    return result