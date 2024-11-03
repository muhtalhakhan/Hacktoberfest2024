# data_visualization.py
# Project: CSV Data Visualizer
# Description: This script provides basic data visualization functions to analyze the cleaned dataset.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_missing_values(df):
    """
    Plot missing values per column in a bar chart.

    Contributors: Customize the chart or add options for displaying in percentage or absolute values.
    """
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if missing.empty:
        print("No missing values in the dataset.")
    else:
        plt.figure(figsize=(10, 5))
        missing.plot(kind='bar', color='skyblue')
        plt.title("Missing Values per Column")
        plt.xlabel("Columns")
        plt.ylabel("Number of Missing Values")
        plt.show()

def plot_numerical_distributions(df):
    """
    Plot distributions of numerical columns.

    Contributors: Add parameters for bin sizes or range customization.
    """
    numeric_cols = df.select_dtypes(include=['number']).columns
    if not numeric_cols.empty:
        df[numeric_cols].hist(bins=15, figsize=(15, 10), color='lightblue')
        plt.suptitle("Distributions of Numerical Columns")
        plt.show()
    else:
        print("No numerical columns to display.")

def plot_correlation_heatmap(df):
    """
    Plot a heatmap of correlations among numerical columns.

    Contributors: Enhance this function to support different correlation methods or interactive visualizations.
    """
    numeric_cols = df.select_dtypes(include=['number']).columns
    if not numeric_cols.empty:
        plt.figure(figsize=(10, 8))
        correlation = df[numeric_cols].corr()
        sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title("Correlation Heatmap")
        plt.show()
    else:
        print("No numerical columns for correlation heatmap.")

def main():
    # Path to the cleaned dataset
    file_path = 'path/to/your/cleaned_dataset.csv'
    
    # Load the cleaned dataset
    df = pd.read_csv(file_path)
    
    # Generate visualizations
    plot_missing_values(df)
    plot_numerical_distributions(df)
    plot_correlation_heatmap(df)

if __name__ == '__main__':
    main()
