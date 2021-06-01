from typing import Optional
from pydantic import BaseModel, Field
import datetime
import array


class RawCalibration(BaseModel):
    raw: float
    calibrated: float


class LocationAQISchema(BaseModel):
    area: str = None
    latitude: Optional[RawCalibration] = None
    longitude: Optional[RawCalibration] = None
    updated: datetime.datetime = None
    PM2_5: Optional[RawCalibration] = None
    temperature: Optional[RawCalibration] = None
    humidity: Optional[RawCalibration] = None
    status: str = None
    activities: str = None
    rank: int = None
    history: list = []
