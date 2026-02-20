# Tick Tracking Application (MVP)

This repository contains the MVP implementation of the backend for the Tick Tracking Application API. It processes tick sighting data from an Excel file and exposes it via a RESTful API.

## Project Structure

```
backend/
├── main.py              # Application entry point
├── ingest_data.py       # Script to load Excel data into SQLite
├── core/
│   └── database.py      # Database connection & configuration
├── models/
│   └── tick_data.py     # SQLModel data definition
├── routers/
│   └── sightings.py     # API endpoints for retrieving data
└── ticks.db             # SQLite database (generated)
data/
└── Tick Sightings.xlsx  # Raw data source
```

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
