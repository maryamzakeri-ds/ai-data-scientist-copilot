import pandas as pd
import numpy as np

def remove_duplicates(df):
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    removed = before - after
    message = f'{removed} duplicate rows removed.'
    return df, message

def statndardize_missing_values(df):
    before = df.isna().sum().sum()
    missing_patterns = ['', ' ', 'NA', 'N/A', 'null', 'None']
    df = df.replace(missing_patterns, np.nan)
    after = df.isna().sum().sum()
    missing = after - before
    message = f'{missing} missing values standardized.'
    return df, message

def trim_text_columns(df):
    text_columns = df.select_dtypes(include=['str']).columns
    for col in text_columns:
        df[col] = df[col].str.strip()
    message = 'Text columns trimmed.'
    return df, message

def convert_numeric_columns(df, threshold=0.8):
    before = len(df.select_dtypes(include=['number']).columns)
    for col in df.columns:
        converted = pd.to_numeric(df[col], errors='coerce')
        ratio = converted.notna().mean()
        if ratio >= threshold:
            df[col] = converted
    after = len(df.select_dtypes(include=['number']).columns)
    message = f'{after-before} columns converted to numeric'
    return df, message

def remove_empty_rows(df):
    before = len(df)
    df = df.dropna(how='all')
    after = len(df)
    removed = before - after
    message = f'{removed} empty rows removed.'
    return df, message

def remove_empty_columns(df):
    before = len(df)
    df = df.dropna(axis=1, how='all')
    after = len(df)
    removed = before - after
    message = f'{removed} empty columns removed.'
    return df, message

def normalize_column_names(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(r'\s+', '_', regex=True)
        .str.replace(r'[^a-z0-9_]', '_', regex=True)
        .str.replace(r'_+', '_', regex=True)
    )
    message = 'Column names normalized.'
    return df, message

def clean_dataset(df):
    reports = []

    df, message = normalize_column_names(df)
    reports.append(message)

    df, message = trim_text_columns(df)
    reports.append(message)

    df, message = statndardize_missing_values(df)
    reports.append(message)

    df, message = remove_duplicates(df)
    reports.append(message)

    df, message = convert_numeric_columns(df)
    reports.append(message)

    df, message = remove_empty_rows(df)
    reports.append(message)

    df, message = remove_empty_columns(df)
    reports.append(message)

    return df, reports
