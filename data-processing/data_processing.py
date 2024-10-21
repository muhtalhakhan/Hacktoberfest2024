import pandas as pd
import sys
import os

def load_data(file_path):
    """Loads the dataset from a file, supports CSV and Excel."""
    file_extension = os.path.splitext(file_path)[1]
    try:
        if file_extension == '.csv':
            df = pd.read_csv(file_path)
        elif file_extension in ['.xls', '.xlsx']:
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Only CSV and Excel are supported.")
        
        print(f"Dataset loaded successfully. {df.shape[0]} rows and {df.shape[1]} columns.")
        return df
    except Exception as e:
        print(f"Error loading dataset: {e}")
        sys.exit(1)

def handle_missing_data(df, method='mean'):
    """Handles missing data by filling with mean, median, or dropping rows, only for numeric columns."""
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
    """Removes duplicate rows from the dataset."""
    initial_rows = df.shape[0]
    df.drop_duplicates(inplace=True)
    final_rows = df.shape[0]
    print(f"Removed {initial_rows - final_rows} duplicate rows.")
    return df

def normalize_data(df):
    """Normalizes numeric data and date formats."""
    for col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = pd.to_numeric(df[col], errors='coerce')
        elif pd.api.types.is_datetime64_any_dtype(df[col]) or 'date' in col.lower():
            df[col] = pd.to_datetime(df[col], errors='coerce')
    print("Data normalized.")
    return df

def save_cleaned_data(df, file_path):
    """Saves the cleaned dataset to a new file."""
    clean_file_path = file_path.replace('.csv', '_cleaned.csv').replace('.xlsx', '_cleaned.xlsx')
    file_extension = os.path.splitext(file_path)[1]
    
    if file_extension == '.csv':
        df.to_csv(clean_file_path, index=False)
    elif file_extension in ['.xls', '.xlsx']:
        df.to_excel(clean_file_path, index=False)
    
    print(f"Cleaned dataset saved to {clean_file_path}")

def print_summary(df):
    """Prints a summary of the dataset including number of rows, columns, and data types."""
    print("\nDataset Summary:")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print("\nColumn Data Types:")
    print(df.dtypes)
    print("\nMissing Values per Column:")
    print(df.isnull().sum())

def main():
    file_path = r'C:\Users\Venky\Desktop\Lab\example.csv'  # Path to your file
    df = load_data(file_path)
    
    print_summary(df)  # Print summary of the dataset

    df = handle_missing_data(df, method='mean')
    df = remove_duplicates(df)
    df = normalize_data(df)
    
    save_cleaned_data(df, file_path)

if __name__ == '__main__':
    main()
