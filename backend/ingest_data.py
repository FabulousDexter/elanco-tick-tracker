import pandas as pd
from sqlmodel import Session, select
from core.database import engine, create_db_and_tables
from models.tick_data import TickData
import os
from datetime import datetime


def ingest_excel_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return

    print("Creating database and tables...")
    create_db_and_tables()

    print(f"Reading Excel file: {file_path}...")
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return

    print(
        f"Found {len(df)} rows in the Excel file. Ingesting data into the database..."
    )

    with Session(engine) as session:
        # Check if data already exists to avoid duplicates
        existing = session.exec(select(TickData), limit=1).first()
        if existing:
            print("Data already exists in the database. Skipping ingestion.")
            return

        for index, row in df.iterrows():
            try:
                # Handling data parsing
                date_val = row.get("date")
                timestamp = None

                # If date is string, parse it. If datetime object, use it directly.
                if isinstance(date_val, str):
                    try:
                        # Try standard date formats (e.g. 2022-08-01T06:40:31)
                        timestamp = datetime.strptime(date_val, "%Y-%m-%dT%H:%M:%S")
                    except ValueError:
                        # Fallback to ISO format
                        timestamp = datetime.fromisoformat(date_val)
                else:
                    timestamp = date_val

                # Create TickData object matching our model
                tick_entry = TickData(
                    id=str(row.get("id")),
                    timestamp=timestamp,
                    location=str(row.get("location")),
                    species=str(row.get("species")),
                    latin_name=str(row.get("latinName")),
                )
                session.add(tick_entry)
            except Exception as e:
                print(f"Skipping row {index} due to error: {e}")
                continue

        session.commit()
        print("Data ingestion completed successfully.")


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "data", "Tick Sightings.xlsx")

    ingest_excel_file(file_path)
