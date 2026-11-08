import pandas as pd

def get_missing_values(df):
    missing = {}
    for col in df.columns:
        null_count = df[col].isna().sum()
        if null_count:
            missing[col] = int(null_count)

        if df[col].dtype == 'str':
            empty_str_count = (df[col].str.strip() == '').sum()
            if empty_str_count:
                missing[col] = int(empty_str_count)

    return missing

def is_numerical(column, threshold=0.8):
    converted = pd.to_numeric(column, errors='coerce')
    ratio = converted.notna().mean()
    if ratio >= threshold:
        return True
    else:
        return False

def is_boolean(column):
    unique_values = column.dropna().unique()
    if len(unique_values) != 2:
        return False

    boolean_sets = [
        {True, False},
        {0, 1},
        {'Yes', 'No'},
        {'yes', 'no'},
        {'Y', 'N'},
        {'y', 'n'}
    ]
    return set(unique_values) in boolean_sets

def is_identifier(column, threshold=0.95):
    if len(column) == 0:
        return False

    ratio = column.nunique(dropna=True) / len(column)
    return ratio >= threshold


def get_data_types(df):
    numeric_columns = []
    boolean_columns = []
    identifier_columns = []
    categorical_columns = []

    for col in df.columns:
        if is_boolean(df[col]):
            boolean_columns.append(col)

        elif is_identifier(df[col]):
            identifier_columns.append(col)

        elif is_numerical(df[col]):
            numeric_columns.append(col)

        else:
            categorical_columns.append(col)

    return {
        'boolean': boolean_columns,
        'identifier': identifier_columns,
        'numeric': numeric_columns,
        'categorical': categorical_columns
    }


def profile_dataset(df):
    return {
        'rows': int(len(df)),
        'columns': int(len(df.columns)),
        'missing_values': get_missing_values(df),
        'duplicates':int(df.duplicated().sum()),
        'data_types': get_data_types(df)
    }

