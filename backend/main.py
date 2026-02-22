from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from core.database import create_db_and_tables
from routers import sightings
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Tick Tracking API",
    description="API for tracking tick sightings across the UK.",
    version="1.0.0",
)


app.include_router(sightings.router)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global exception: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error", "details": str(exc)},
    )


@app.get("/")
def read_root():
    return {"message": "Welcome to the Elanco Tick Tracking API"}


@app.on_event("startup")
def startup_event():
    create_db_and_tables()
