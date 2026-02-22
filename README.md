# Elanco Tick Tracking Application (MVP)

Welcome to the backend service for the Elanco Tick Tracking Application. This system is designed to ingest, store, and analyze tick sighting data.

This project implements a RESTful API that allows users to search for sightings and view aggregated reports on regional activity and trends over time.

## Project Structure

```
backend/
├── main.py              # Application entry point & Global Error Handling
├── ingest_data.py       # Data Pipeline (Cleaning, Validation, Ingestion)
├── core/
│   └── database.py      # Database connection & configuration
├── models/
│   └── tick_data.py     # SQLModel schema definition
├── routers/
│   └── sightings.py     # API controllers for Sightings and Reports
└── ticks.db             # SQLite database (auto-generated)
data/
└── Tick Sightings.xlsx  # Raw data source
```

## Key Features

- **Data Ingestion**: Processes Excel datasets with duplicate checks and validation for missing data.
- **Search & Filtering**: Case-insensitive filtering for location and species.
- **Date Filtering**: Supports filtering sightings by specific date ranges.
- **Data Reporting**: Endpoints for regional sighting counts and monthly trends.
- **Error Handling**: Implements global exception handling.

## Prerequisites

- Python 3.9+
- `pip`

## Setup & Installation

1.  **Clone the repository** (if applicable) or navigate to the project root.

2.  **Create a virtual environment**:
    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment**:
    - Windows (PowerShell):
      ```powershell
      .\.venv\Scripts\Activate.ps1
      ```
    - macOS/Linux:
      ```bash
      source .venv/bin/activate
      ```

4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Data Ingestion

Before starting the server, you must populate the database with the provided Excel data.

1.  Navigate to the project root.
2.  Run the ingestion script:
    ```bash
    python backend/ingest_data.py
    ```
    *This will create `backend/ticks.db` and populate it with data from `data/Tick Sightings.xlsx`.*

## Running the Server

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```

2.  Start the Uvicorn server:
    ```bash
    uvicorn main:app --reload
    ```

The API will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## API Documentation

Once the server is running, you can access the interactive API documentation:

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### 1. **Get All Sightings**
- **URL:** `GET /sightings`
- **Query Parameters:**
    - `location` (optional): Filter by city name (e.g., `London`).
    - `species` (optional): Filter by tick species (e.g., `Marsh tick`).
    - `limit` (default: 100): Number of records to return.
    - `offset` (default: 0): Pagination offset.

**Example Request:**
```bash
curl "http://127.0.0.1:8000/sightings?location=London&limit=5"
```

### 2. **Get Sighting by ID**
- **URL:** `GET /sightings/{id}`
- **Example Request:**
    ```bash
    curl http://127.0.0.1:8000/sightings/02WNholuSg6ndCk4c1dA
    ```

## Tech Stack
- **Framework:** FastAPI
- **Database:** SQLite (via SQLModel)
- **Data Processing:** Pandas
