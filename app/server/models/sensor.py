from typing import Optional
from pydantic import BaseModel, Field
import datetime


class RawCalibration(BaseModel):
    raw: float
    calibrated: float


class SensorSchema(BaseModel):
    device_id: int = None
    updated: datetime.datetime = None
    latitude: Optional[RawCalibration] = None
    longitude: Optional[RawCalibration] = None
    PM2_5: Optional[RawCalibration] = None
    PM10: Optional[RawCalibration] = None
    PM1_0: Optional[RawCalibration] = None
    temperature: Optional[RawCalibration] = None
    humidity: Optional[RawCalibration] = None
    CO: Optional[RawCalibration] = None
    CO2: Optional[RawCalibration] = None
    NO2: Optional[RawCalibration] = None
    O3: Optional[RawCalibration] = None
    SO2: Optional[RawCalibration] = None
