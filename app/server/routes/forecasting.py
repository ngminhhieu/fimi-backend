from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.dms.forecasting import (
    add_forecasting,
    delete_forecasting,
    retrieve_forecasting,
    retrieve_forecastings,
    update_forecasting,
)
from server.utils.response import (
    ErrorResponseModel,
    ResponseModel,
)
from server.models.forecasting import ForecastingSchema

router = APIRouter()

@router.get("/", response_description="forecastings retrieved")
async def get_forecastings():
    forecastings = await retrieve_forecastings()
    if forecastings:
        return ResponseModel(forecastings, "forecastings data retrieved successfully")
    return ResponseModel(forecastings, "Empty list returned")


@router.get("/{area}", response_description="forecasting data retrieved")
async def get_forecasting_data(area):
    forecasting = await retrieve_forecasting(area)
    if forecasting:
        return ResponseModel(forecasting, "forecasting data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "forecasting doesn't exist.")


@router.post("/", response_description="forecasting data added into the database")
async def add_forecasting_data(forecasting: ForecastingSchema = Body(...)):
    forecasting = jsonable_encoder(forecasting)
    new_forecasting = await add_forecasting(forecasting)
    return ResponseModel(new_forecasting, "forecasting added successfully.")


@router.delete("/{area}", response_description="forecasting data deleted from the database")
async def delete_forecasting_data(area: str):
    deleted_forecasting = await delete_forecasting(area)
    if deleted_forecasting:
        return ResponseModel(
            "forecasting with area: {} removed".format(area), "forecasting deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "forecasting with area {0} doesn't exist".format(area)
    )
