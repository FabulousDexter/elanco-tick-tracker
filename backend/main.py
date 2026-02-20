from fastapi import FastAPI
from core.database import create_db_and_tables
from routers import sightings

app = FastAPI(
    title="Tick Tracking API",
    description="API for tracking tick sightings across the UK.",
    version="1.0.0",
)


app.include_router(sightings.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Elanco Tick Tracking API"}


@app.on_event("startup")
def startup_event():
    create_db_and_tables()
