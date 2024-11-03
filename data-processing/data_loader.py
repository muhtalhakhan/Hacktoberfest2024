# Project: CSV Data Cleaner
# Description: This Python script processes datasets (CSV, Excel, and JSON files) by cleaning missing data, removing duplicates, and normalizing formats.
# Author: Maisagalla Venkatesh

import pandas as pd
import sys
import os

def load_data(file_path):
    """
    Load dataset from a file. Supports CSV, Excel, and JSON formats.

    Contributors: Extend to support additional file types (e.g., XML, Parquet) or integrate an API for remote datasets.
    """
    file_extension = os.path.splitext(file_path)[1]
    try:
        if file_extension == '.csv':
            df = pd.read_csv(file_path)
        elif file_extension in ['.xls', '.xlsx']:
            df = pd.read_excel(file_path)
        elif file_extension == '.json':
            df = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format. Supported formats are CSV, Excel, and JSON.")
        
        print(f"Dataset loaded successfully. {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)

def handle_missing_data(df, method='mean'):
    """
    Handle missing data by filling numeric columns with mean, median, or dropping rows.

    Contributors: Add advanced techniques like interpolation or ML-based imputation.
    """
    numeric_cols = df.select_dtypes(include=['number']).columns
    if method == 'mean':
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    elif method == 'median':
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    elif method == 'drop':
        df.dropna(inplace=True)
    else:
        print("Invalid method specified. Using mean as default.")
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    print("Missing data handled.")
    return df

def remove_duplicates(df):
    """
    Remove duplicate rows.

    Contributors: Allow specification of columns for duplicate checking.
    """
    initial_rows = df.shape[0]
    df.drop_duplicates(inplace=True)
    final_rows = df.shape[0]
    print(f"Removed {initial_rows - final_rows} duplicate rows.")
    return df

def normalize_data(df):
    """
    Normalize numeric data and date formats.

    Contributors: Add more normalization options like min-max scaling or standardization.
    """
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = pd.to_numeric(df[col], errors='coerce')
        elif pd.api.types.is_datetime64_any_dtype(df[col]) or 'date' in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce')
    print("Data normalized.")
    return df

def save_cleaned_data(df, file_path):
    """
    Save the cleaned dataset in CSV, Excel, or JSON format.

    Contributors: Support additional formats like Parquet, or cloud/database storage.
    """
    clean_file_path = file_path.replace('.csv', '_cleaned.csv').replace('.xlsx', '_cleaned.xlsx').replace('.json', '_cleaned.json')
    file_extension = os.path.splitext(file_path)[1]
    try:
        if file_extension == '.csv':
            df.to_csv(clean_file_path, index=False)
        elif file_extension in ['.xls', '.xlsx']:
            df.to_excel(clean_file_path, index=False)
        elif file_extension == '.json':
            df.to_json(clean_file_path, orient='records')
        
        print(f"Cleaned dataset saved to {clean_file_path}")
    except Exception as e:
        print(f"Error saving cleaned dataset: {e}")

def print_summary(df):
    """
    Print a summary of the dataset: rows, columns, data types, and missing values.

    Contributors: Add visualizations for data distribution or more insights.
    """
    print("\nDataset Summary:")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print("\nColumn Data Types:")
    print(df.dtypes)
    print("\nMissing Values per Column:")
    print(df.isnull().sum())

def main():
    # Update this file path as needed
    file_path = 'path/to/your/dataset.csv'
    
    # Load the dataset
    df = load_data(file_path)

    # Print dataset summary
    print_summary(df)

    # Handle missing data
    df = handle_missing_data(df, method='mean')

    # Remove duplicates
    df = remove_duplicates(df)

    # Normalize data
    df = normalize_data(df)

    # Save cleaned data
    save_cleaned_data(df, file_path)

if __name__ == '__main__':
    main()
