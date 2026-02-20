from fastapi import APIRouter, Depends, Query, HTTPException
from sqlmodel import Session, select, func
from typing import List, Optional
from core.database import get_session
from models.tick_data import TickData

router = APIRouter(
    prefix="/sightings",
    tags=["sightings"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[TickData])
def read_sightings(
    session: Session = Depends(get_session),
    location: Optional[str] = None,
    species: Optional[str] = None,
    limit: int = 100,
    offset: int = 0,
):
    statement = select(TickData)

    if location:
        statement = statement.where(TickData.location == location)
    if species:
        statement = statement.where(TickData.species == species)

    statement = statement.offset(offset).limit(limit)
    results = session.exec(statement).all()
    return results


@router.get("/{id}", response_model=TickData)
def read_sighting_by_id(id: str, session: Session = Depends(get_session)):
    sighting = session.get(TickData, id)
    if not sighting:
        raise HTTPException(status_code=404, detail="Sighting not found")
    return sighting


@router.get("/reports/region", tags=["reports"])
def get_sightings_by_region(session: Session = Depends(get_session)):
    # This query groups sightings by location and counts them
    statement = select(
        TickData.location, func.count(TickData.id).label("sighting_count")
    ).group_by(TickData.location)

    results = session.exec(statement).all()

    # Format the result into clean list of disctionaries
    report = [{"region": row[0], "total_sightings": row[1]} for row in results]
    return report
