from fastapi import FastAPI

from server.routes.sensor import router as SensorRouter
from server.routes.forecasting import router as ForecastingRouter
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


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
