import pandas as pd
from pathlib import Path


def view_dataset(df):
    return df


def dataset_info(df):
    info = {
        "Rows": df.shape[0],
        "Columns": df.shape[1],
        "Column Names": list(df.columns),
        "Data Types": df.dtypes
    }
    
    return info


def remove_duplicates(df):
    df = df.drop_duplicates()
    return df


def replace_missing_val(df, fill_value):
    df = df.fillna(fill_value)
    return df


def sort_by_column(df, selected_column, ascending=True):
    df = df.sort_values(
        by=selected_column,
        ascending=ascending
    )

    return df


def export_csv(df, output_path):
    df.to_csv(output_path, index=False)