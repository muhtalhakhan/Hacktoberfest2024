import pandas as pd

# Load CSV file
def load_csv(file_path):
    try:
        data = pd.read_csv(file_path)
        print("CSV file loaded successfully!")
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

# Process the data: Handle missing values, remove duplicates, normalize formats
def clean_csv(data):
    if data is not None:
        # Fill missing values with a placeholder or a default value
        data.fillna("N/A", inplace=True)
        
        # Remove duplicate rows
        data.drop_duplicates(inplace=True)
        
        # Normalize date formats (if there's a date column, adjust accordingly)
        # Example: Standardize to 'YYYY-MM-DD' format
        # Assuming 'Date' is a column in the CSV
        if 'Date' in data.columns:
            data['Date'] = pd.to_datetime(data['Date'], errors='coerce').dt.strftime('%Y-%m-%d')
        
        print("Data cleaned successfully!")
        return data
    else:
        print("No data to process.")
        return None

# Save cleaned data back to a CSV file
def save_cleaned_csv(data, output_file_path):
    if data is not None:
        data.to_csv(output_file_path, index=False)
        print(f"Cleaned CSV saved to {output_file_path}")
    else:
        print("No data to save.")

# Example usage
file_path = '/Users/sankshay/Downloads/MacPorts-2.9.0/vendor/tcllib-1.21/examples/csv/Benchmark.805.csv'  # Change to the actual file path
output_file_path = '/Users/sankshay/Downloads/example.csv'

csv_data = load_csv(file_path)
cleaned_data = clean_csv(csv_data)
save_cleaned_csv(cleaned_data, output_file_path)
