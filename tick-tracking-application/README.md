# Tick Tracking Application

This project is designed to track tick sightings and provide insights through a web API. It utilizes a SQLite database for storage and FastAPI for serving the API.

## Project Structure

```
tick-tracking-application
├── inspection
│   └── inspect_data.py
├── data
│   └── Tick Sightings.xlsx
├── requirements.txt
└── README.md
```

## Requirements

The project requires the following Python packages:

- pandas
- openpyxl
- sqlalchemy
- aiosqlite

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Usage

### Inspecting Data

To inspect the columns of the Excel file `Tick Sightings.xlsx`, run the following command:

```
python inspection/inspect_data.py
```

This script will load the Excel file and print out the names of the columns, allowing you to understand the structure of the data.

### Data Ingestion

The application includes a script to ingest data from the Excel file into the SQLite database. This can be run separately to control when data is loaded.

### API Endpoints

The application exposes the following API endpoints:

- `GET /sightings`: Retrieve tick sightings filtered by date range, location, and species.
- `GET /stats`: Aggregate data to provide counts by region and sightings over time.

## Database

The application uses SQLite as the database for simplicity and portability. The database schema is defined using SQLAlchemy.

## Contribution

Feel free to contribute to this project by submitting issues or pull requests.