from fastapi import APIRouter, HTTPException, Depends, Query
from sqlmodel import Session, select
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


@router.get("/{sighting_id}", response_model=TickData)
def read_sighting_id(id: str, session: Session = Depends(get_session)):
    sighting = session.get(TickData, id)
    if not sighting:
        raise HTTPException(status_code=404, detail="Sighting not found")
    return sighting
