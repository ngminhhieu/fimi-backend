from fastapi import FastAPI

from server.routes.sensor import router as SensorRouter
from server.routes.forecasting import router as ForecastingRouter
from server.routes.location_aqi import router as LocationAQIRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(SensorRouter, tags=["Sensor"], prefix="/sensor")
app.include_router(ForecastingRouter, tags=["Forecasting"], prefix="/forecasting")
app.include_router(LocationAQIRouter, tags=["Location AQI"], prefix="/aqi")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
