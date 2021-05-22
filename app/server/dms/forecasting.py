import motor.motor_asyncio
from bson import ObjectId
from decouple import config
from typing import Optional
from server.database.mongo import database

forecasting_collection = database.get_collection("forecasting")

# helpers
def forecasting_helper(forecasting) -> dict:
    return {
        "id": str(forecasting["_id"]),
        "area": forecasting["device_id"],
        "datetime": forecasting["datetime"],
        "PM2_5": forecasting["PM2_5"],
        "PM10": forecasting["PM10"],
        "PM1_0": forecasting["PM1_0"],
        "temperature": forecasting["temperature"],
        "humidity": forecasting["humidity"],
        "CO": forecasting["CO"],
        "CO2": forecasting["CO2"],
        "NO2": forecasting["NO2"],
        "O3": forecasting["O3"],
        "SO2": forecasting["SO2"],
    }


async def retrieve_forecastings():
    forecastings = []
    async for forecasting in forecasting_collection.find().limit(20):
        forecastings.append(forecasting_helper(forecasting))
    return forecastings

async def add_forecasting(forecasting_data: dict) -> dict:
    forecasting = await forecasting_collection.insert_one(forecasting_data)
    new_forecasting = await forecasting_collection.find_one({"_id": forecasting.inserted_id})
    return forecasting_helper(new_forecasting)

async def retrieve_forecasting(id: str) -> dict:
    forecasting = await forecasting_collection.find_one({"device_id": id})
    if forecasting:
        return forecasting_helper(forecasting)

async def update_forecasting(id: str, data: dict):
    if len(data) < 1:
        return False
    forecasting = await forecasting_collection.find_one({"device_id": id})
    if forecasting:
        updated_forecasting = await forecasting_collection.update_one(
            {"device_id": id}, {"$set": data}
        )
        if updated_forecasting:
            return True
        return False

async def delete_forecasting(id: str):
    forecasting = await forecasting_collection.find_one({"device_id": id})
    if forecasting:
        await forecasting_collection.delete_one({"device_id": id})
        return True