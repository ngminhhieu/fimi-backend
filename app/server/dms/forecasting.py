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
        "device_id": forecasting["device_id"],
        "area": forecasting["area"],
        "latitude": forecasting["latitude"],
        "longitude": forecasting["longitude"],
        "updated": forecasting["updated"],
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
    async for forecasting in forecasting_collection.aggregate([
        {'$sort': {'updated': -1}},
            {'$group': {'_id': {'device_id': '$device_id'}, "doc": {"$first": "$$ROOT"}}}]):
        forecastings.append(forecasting_helper(forecasting['doc']))
    return forecastings


async def add_forecasting(forecasting_data: dict) -> dict:
    forecasting = await forecasting_collection.insert_one(forecasting_data)
    new_forecasting = await forecasting_collection.find_one({"_id": forecasting.inserted_id})
    return forecasting_helper(new_forecasting)


async def retrieve_forecasting(area: str) -> dict:
    forecastings = []
    async for forecasting in forecasting_collection.aggregate([
        {'$match': {"area": area}},
        {'$sort': {'updated': -1}},
            {'$group': {'_id': {'device_id': '$device_id'}, "doc": {"$first": "$$ROOT"}}}]):
        forecastings.append(forecasting_helper(forecasting['doc']))
    return forecastings


async def update_forecasting(_id: str, data: dict):
    if len(data) < 1:
        return False
    forecasting = await forecasting_collection.find_one({"_id": _id})
    if forecasting:
        updated_forecasting = await forecasting_collection.update_one(
            {"_id": _id}, {"$set": data}
        )
        if updated_forecasting:
            return True
        return False


async def delete_forecasting(_id: str):
    forecasting = await forecasting_collection.find_one({"_id": _id})
    if forecasting:
        await forecasting_collection.delete_one({"_id": _id})
        return True
