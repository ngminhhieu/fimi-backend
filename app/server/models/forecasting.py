from typing import Optional
from pydantic import BaseModel, Field


class ForecastingSchema(BaseModel):
    area: str = None
    datetime: str = None
    PM2_5: float = None
    PM10: float = None
    PM1_0: float = None
    temperature: float = None
    humidity: float = None
    CO: float = None
    CO2: float = None
    NO2: float = None
    O3: float = None
    SO2: float = None