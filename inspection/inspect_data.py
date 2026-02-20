import pandas as pd
import os


def inspect_excel_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    try:
        print(f"--- Loading Excel file: {file_path} ---")

        # Load the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        print("\n--- Column Names ---")
        for column in df.columns:
            print(column)

        print("\n--- Data Types of Each Column ---")
        print(df.dtypes)

        print("\n--- First 5 rows ---")
        print(df.head().to_string())

        print("\n--- Summary Statistics ---")
        print(df.describe(include="all").to_string())

    except Exception as e:
        print(f"Error reading file: {e}")


if __name__ == "__main__":
    file_path = "backend/data/Tick Sightings.xlsx"
    inspect_excel_file(file_path)
