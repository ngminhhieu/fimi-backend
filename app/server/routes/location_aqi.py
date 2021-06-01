from typing import Optional
from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.dms.location_aqi import (
    add_location_aqi,
    delete_aqi,
    retrieve_location_aqi,
    retrieve_location_aqis,
    update_location_aqi,
)
from server.utils.response import (
    ErrorResponseModel,
    ResponseModel,
)
from server.models.location_aqi import LocationAQISchema

router = APIRouter()


@router.get("/get_aqis", response_description="locations aqis retrieved")
async def get_loc_aqis():
    aqis = await retrieve_location_aqis()
    if aqis:
        return ResponseModel(aqis, "locations aqis data retrieved successfully")
    return ResponseModel(aqis, "Empty list returned")


@router.get("/get_aqi_by_area/{area}", response_description="location aqi data retrieved")
async def get_loc_aqi_data(area: str, lat: Optional[float] = None, long: Optional[float] = None):
    aqi = await retrieve_location_aqi(area, lat, long)
    if aqi:
        return ResponseModel(aqi, "location aqi data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Do not have that aqi info at location.")


@router.post("/add_aqi", response_description="aqi data added into the database")
async def add_aqi_data(aqi: LocationAQISchema = Body(...)):
    aqi = jsonable_encoder(aqi)
    new_aqi = await add_location_aqi(aqi)
    return ResponseModel(new_aqi, "aqi added successfully.")


@router.post("/update_aqi_by_id", response_description="update aqi")
async def update_aqi_data(aqi: LocationAQISchema = Body(...)):
    aqi = jsonable_encoder(aqi)
    updated_aqi = await update_location_aqi(aqi["_id"], aqi)
    if updated_aqi:
        return ResponseModel(updated_aqi, "aqi updated successfully.")
    return ErrorResponseModel(
        "An error occurred", 404, "aqi with _id {0} doesn't exist".format(aqi["_id"])
    )


@router.delete("/delete_aqi/{id}", response_description="aqi data deleted from the database")
async def delete_aqi_data(id: str):
    deleted_aqi = await delete_aqi(id)
    if deleted_aqi:
        return ResponseModel(
            "aqi with id: {} removed".format(id), "aqi deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "aqi with id {0} doesn't exist".format(id)
    )
