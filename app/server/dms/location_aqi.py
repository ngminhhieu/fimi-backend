import motor.motor_asyncio
from bson import ObjectId
from decouple import config
from typing import Optional
from server.database.mongo import database

locationaqi_collection = database.get_collection("location_aqi")

# helpers


def location_aqi_helper(aqi) -> dict:
    return {
        "id": str(aqi["_id"]),
        "area": aqi["area"],
        "updated": aqi["updated"],
        "latitude": aqi["latitude"],
        "longitude": aqi["longitude"],
        "PM2_5": aqi["PM2_5"],
        "temperature": aqi["temperature"],
        "humidity": aqi["humidity"],
        "status": aqi["status"],
        "activities": aqi["activities"],
        "rank": aqi["rank"],
        "history": aqi["history"]
    }


def heatmap_helper(aqi) -> dict:
    return {
        "latitude": aqi["latitude"],
        "longitude": aqi["longitude"],
        "updated": aqi["updated"],
        "PM2_5": aqi["PM2_5"]
    }


async def retrieve_location_aqis():
    aqis = []
    async for aqi in locationaqi_collection.find().limit(20):
        print(aqi['updated'])
        aqis.append(location_aqi_helper(aqi))
    return aqis


async def retrieve_heatmaps():
    heatmaps = []
    async for heatmap in locationaqi_collection.find().limit(20):
        heatmaps.append(heatmap_helper(heatmap))

    return heatmaps


async def add_location_aqi(aqi_data: dict) -> dict:
    history = retrieve_location_aqi(aqi_data['area'], aqi_data['latitude'], aqi_data['longitude'])
    aqi_data['history'] = [his['PM2.5'] for his in history]
    aqi = await locationaqi_collection.insert_one(aqi_data)
    new_aqi = await locationaqi_collection.find_one({"_id": aqi.inserted_id})
    return location_aqi_helper(new_aqi)


async def retrieve_location_aqi(area: str, lat: float = None, long: float = None) -> dict:
    aqis = []
    if lat is not None and long is not None:
        async for aqi in locationaqi_collection.find({"area": area, "latitude": lat, "longitude": long}):
            aqis.append(location_aqi_helper(aqi))
    else:
        async for aqi in locationaqi_collection.find({"area": area}):
            aqis.append(location_aqi_helper(aqi))
    return aqis[len(aqis) - 1]  # return the latest record


async def update_location_aqi(_id: str, data: dict):
    if len(data) < 1:
        return False
    aqi = await locationaqi_collection.find_one({"_id": _id})
    if aqi:
        updated_aqi = await locationaqi_collection.update_one(
            {"_id": _id}, {"$set": data}
        )
        if update_location_aqi:
            return True
        return False


async def delete_aqi(_id: str):
    aqi = await locationaqi_collection.find_one({"_id": _id})
    if aqi:
        await locationaqi_collection.delete_one({"_id": _id})
        return True

    return False
