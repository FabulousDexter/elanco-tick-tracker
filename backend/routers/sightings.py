from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import Session, select, func
from typing import List, Optional
from datetime import datetime
from core.database import get_session
from models.tick_data import TickData

router = APIRouter(
    prefix="/sightings",
    responses={404: {"description": "Not found"}},
)


@router.get("/", tags=["sightings"], response_model=List[TickData])
def read_sightings(
    session: Session = Depends(get_session),
    location: Optional[str] = None,
    species: Optional[str] = None,
    start_date: Optional[datetime] = None,
    end_date: Optional[datetime] = None,
    limit: int = 100,
    offset: int = 0,
):
    statement = select(TickData)

    if location:
        statement = statement.where(func.lower(TickData.location) == location.lower())
    if species:
        statement = statement.where(func.lower(TickData.species) == species.lower())
    if start_date:
        statement = statement.where(TickData.timestamp >= start_date)
    if end_date:
        statement = statement.where(TickData.timestamp <= end_date)

    statement = statement.offset(offset).limit(limit)
    results = session.exec(statement).all()
    return results


@router.get("/reports/region", tags=["reports"])
def get_sightings_by_region(session: Session = Depends(get_session)):
    """
    Fulfills the requirement: Number of sightings per region.
    """
    statement = (
        select(TickData.location, func.count(TickData.id).label("total_sightings"))
        .group_by(TickData.location)
        .order_by(TickData.location)
    )

    results = session.exec(statement).all()

    report = [{"region": row[0], "total_sightings": row[1]} for row in results]
    return report


@router.get("/reports/trends", tags=["reports"])
def get_sightings_trends(session: Session = Depends(get_session)):
    """
    Fulfills the requirement: Trends over time (monthly).
    """
    # SQLite uses strftime to extract the Year and Month for grouping
    statement = (
        select(
            func.strftime("%Y-%m", TickData.timestamp).label("month"),
            func.count(TickData.id).label("total_sightings"),
        )
        .group_by("month")
        .order_by("month")
    )

    results = session.exec(statement).all()

    report = [{"month": row[0], "total_sightings": row[1]} for row in results]
    return report


@router.get("/{id}", tags=["sightings"], response_model=TickData)
def read_sighting_by_id(id: str, session: Session = Depends(get_session)):
    sighting = session.get(TickData, id)
    if not sighting:
        raise HTTPException(status_code=404, detail="Sighting not found")
    return sighting
