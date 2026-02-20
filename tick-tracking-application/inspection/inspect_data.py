import pandas as pd

def inspect_excel_columns(file_path):
    try:
        # Load the Excel file
        df = pd.read_excel(file_path)

        # Print the column names
        print("Columns in the Excel file:")
        print(df.columns.tolist())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # User trigger required
    excel_file_path = '../data/Tick Sightings.xlsx'  # Adjust path as necessary
    inspect_excel_columns(excel_file_path)