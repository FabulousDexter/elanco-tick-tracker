"""
Application entry point
"""
from fastapi import FastAPI
from backend.routers import sightings

app = FastAPI()

# Include routers
app.include_router(sightings.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Elanco Tick Tracker API"}
