# Project: CSV Data Cleaner
# Description: This Python script processes datasets (CSV, Excel, and JSON files) by cleaning missing data, removing duplicates, and normalizing formats.
# Author: Maisagalla Venkatesh

import pandas as pd
import sys
import os
import json


def load_data(file_path):
    """
    Loads the dataset from a file, supports CSV, Excel, and JSON.

    Contributors: You can extend this function to support more file types (e.g., XML, Parquet) or integrate an API for loading remote datasets.
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
            raise ValueError(
                "Unsupported file format. Supported formats are CSV, Excel, and JSON.")

        print(f"Dataset loaded successfully. {
              df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)


def handle_missing_data(df, method='mean'):
    """
    Handles missing data by filling with mean, median, or dropping rows for numeric columns.
    
    Contributors: You can add more sophisticated missing data handling techniques, such as interpolation, or machine learning imputation methods.
    """
    numeric_cols = df.select_dtypes(include=['number']).columns

    if method == 'mean':
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    elif method == 'median':
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    elif method == 'drop':
        df.dropna(inplace=True)
    else:
        print("Invalid method for handling missing data. Using mean as default.")
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    print("Missing data handled.")
    return df


def remove_duplicates(df):
    """
    Removes duplicate rows from the dataset.

    Contributors: This can be extended to allow users to define which columns should be checked for duplicates.
    """
    initial_rows = df.shape[0]
    df.drop_duplicates(inplace=True)
    final_rows = df.shape[0]
    print(f"Removed {initial_rows - final_rows} duplicate rows.")
    return df


def normalize_data(df):
    """
    Normalizes numeric data and date formats.

    Contributors: Consider adding more normalization options (e.g., min-max scaling or standardization).
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
    Saves the cleaned dataset to a new file in CSV, Excel, or JSON format.

    Contributors: Extend this function to save data in other formats like Parquet, or even push the cleaned data to a cloud storage or database.
    """
    clean_file_path = file_path.replace('.csv', '_cleaned.csv').replace(
        '.xlsx', '_cleaned.xlsx').replace('.json', '_cleaned.json')
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
    Prints a summary of the dataset, including number of rows, columns, and data types.

    Contributors: You can add visualizations to provide more insights into the data distribution or other aspects of the dataset.
    """
    print("\nDataset Summary:")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print("\nColumn Data Types:")
    print(df.dtypes)
    print("\nMissing Values per Column:")
    print(df.isnull().sum())


def main():
    # Path to your file (CSV, Excel, or JSON)
    file_path = r'C:\Users\Venky\Desktop\hacktoctober\Hacktoberfest2024\JavaScript-Apps-Programs\test-data\sample.csv'

    # Loading the dataset
    df = load_data(file_path)

    # Printing the summary of the dataset
    print_summary(df)

    # Handling missing data
    df = handle_missing_data(df, method='mean')

    # Removing duplicates
    df = remove_duplicates(df)

    # Normalizing the data
    df = normalize_data(df)

    # Saving the cleaned data
    save_cleaned_data(df, file_path)


if __name__ == '__main__':
    main()
