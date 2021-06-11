import motor.motor_asyncio
from bson import ObjectId
from decouple import config
from typing import Optional
from server.database.mongo import database
import datetime
from math import sin, cos, sqrt, atan2, radians, exp

locationaqi_collection = database.get_collection("sensor")  # extract the data from the sensor table itself

# helpers


async def location_aqi_helper(aqi) -> dict:
    level = aqi['PM2_5'] / 50
    status = ''
    activity = ''
    rank = await rank_helper(aqi['updated'], aqi['_id'])
    print('rank: ' + str(rank))
    if level <= 1:
        status = 'Good'
        activity = 'Suitable for every activities indoor and outdoor'
    elif level <= 2:
        status = 'Moderate'
        activity = 'Suitable for most activities indoor and outdoor'
    elif level <= 3:
        status = 'Unhealthy for Sensitive Groups'
        activity = 'Sensitive people might be affected with heavy activities'
    elif level <= 4:
        status = 'Unhealthy'
        activity = 'Activities outdoor might be affected for most people'
    elif level <= 6:
        status = 'Very Unhealthy'
        activity = 'Activities outdoor might be affected for all people'
    else:
        status = 'Hazardous'
        activity = 'All activities outdoor should be prohibited'

    return {
        "id": str(aqi["_id"]),
        "area": aqi["area"],
        "updated": aqi["updated"],
        "latitude": aqi["latitude"],
        "longitude": aqi["longitude"],
        "PM2_5": aqi["PM2_5"],
        "temperature": aqi["temperature"],
        "humidity": aqi["humidity"],
        "status": status,
        "activities": activity,
        "rank": rank,
        "history": aqi["history"],
    }


async def rank_helper(updated, id) -> int:
    time_delta = datetime.timedelta(minutes=30)
    rank = 0
    async for aqi in locationaqi_collection.find({'updated': {'$gte': updated - time_delta, '$lt': updated + time_delta}}):
        rank += 1
        if (id == aqi['_id']):
            break

    return rank


def heatmap_helper(aqi) -> dict:
    return {
        "latitude": aqi["latitude"],
        "longitude": aqi["longitude"],
        "updated": aqi["updated"],
        "PM2_5": aqi["PM2_5"]
    }


def distance_helper(lat1, long1, lat2, long2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(long1)
    lat2 = radians(lat2)
    lon2 = radians(long2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def calculate_aqi(dis_list):
    denominator = 0
    for dis in dis_list:
        denominator += 1 / dis['distance']
    print("Now denorm is: " + str(denominator))
    aqi = 0
    for dis in dis_list:
        aqi += ((1 / dis['distance']) / denominator) * dis['PM2_5']

    print("Now aqi is: " + str(aqi))
    return aqi


async def retrieve_location_aqis():
    aqis = []
    async for aqi in locationaqi_collection.aggregate([
        {'$sort': {'updated': -1}},
            {'$group': {'_id': {'device_id': '$device_id'}, "doc": {"$first": "$$ROOT"}}}]):
        print(aqi)
        aqis.append(await location_aqi_helper(aqi['doc']))
        # print(aqi)
    print('finish appending')
    return aqis


async def retrieve_heatmaps():
    heatmaps = []
    async for heatmap in locationaqi_collection.aggregate([
        {'$sort': {'updated': -1}},
            {'$group': {'_id': {'device_id': '$device_id'}, "doc": {"$first": "$$ROOT"}}}]):
        heatmaps.append(heatmap_helper(heatmap['doc']))

    return heatmaps


async def rechieve_heatmap(latitude: float, longitude: float):
    heatmaps = []
    async for heatmap in locationaqi_collection.aggregate([
        {'$sort': {'updated': -1}},
            {'$group': {'_id': {'device_id': '$device_id'}, "doc": {"$first": "$$ROOT"}}}]):
        heatmaps.append({
            'distance': distance_helper(latitude, longitude, heatmap['doc']['latitude'], heatmap['doc']['longitude']),
            'PM2_5': heatmap['doc']['PM2_5'],
        })

    # sort the list with asc distance
    def sort_func(ar):
        return ar['distance']

    heatmaps.sort(key=sort_func)

    # calculate the point
    fin_aqi = calculate_aqi(heatmaps[-3:])

    return {
        "latitude": latitude,
        "longitude": longitude,
        "updated": datetime.datetime.now(),
        "PM2_5": fin_aqi
    }


async def add_location_aqi(aqi_data: dict) -> dict:
    history = retrieve_aqis(aqi_data['area'], aqi_data['latitude'], aqi_data['longitude'])
    aqi_data['history'] = [his['PM2.5'] for his in history]
    aqi = await locationaqi_collection.insert_one(aqi_data)
    new_aqi = await locationaqi_collection.find_one({"_id": aqi.inserted_id})
    return await location_aqi_helper(new_aqi)


async def retrieve_location_aqi(area: str, lat: float = None, long: float = None) -> dict:
    aqis = []
    if lat is not None and long is not None:
        # async for aqi in locationaqi_collection.find({"area": area, "latitude": lat, "longitude": long}):
        async for aqi in locationaqi_collection.aggregate([
            {'$match': {"area": area, "latitude": lat, "longitude": long}},
            {'$sort': {'updated': -1}},
                {'$group': {'_id': {'device_id': '$device_id'}, "doc": {"$first": "$$ROOT"}}}]):
            aqis.append(await location_aqi_helper(aqi['doc']))
    else:
        async for aqi in locationaqi_collection.aggregate([
            {'$match': {"area": area}},
            {'$sort': {'updated': -1}},
                {'$group': {'_id': {'device_id': '$device_id'}, "doc": {"$first": "$$ROOT"}}}]):
            aqis.append(await location_aqi_helper(aqi['doc']))
    if (len(aqis) > 0):
        return aqis[len(aqis) - 1]  # return the latest record
    else:
        return {}


async def retrieve_aqis(area: str, lat: float = None, long: float = None) -> dict:
    aqis = []
    if lat is not None and long is not None:
        # async for aqi in locationaqi_collection.find({"area": area, "latitude": lat, "longitude": long}):
        async for aqi in locationaqi_collection.aggregate([
            {'$match': {"area": area, "latitude": lat, "longitude": long}},
            {'$sort': {'updated': -1}},
                {'$group': {'_id': {'device_id': '$device_id'}, "doc": {"$first": "$$ROOT"}}}]):
            aqis.append(await location_aqi_helper(aqi['doc']))
    else:
        async for aqi in locationaqi_collection.aggregate([
            {'$match': {"area": area}},
            {'$sort': {'updated': -1}},
                {'$group': {'_id': {'device_id': '$device_id'}, "doc": {"$first": "$$ROOT"}}}]):
            aqis.append(await location_aqi_helper(aqi['doc']))
    if (len(aqis) > 0):
        return aqis  # return the latest record
    else:
        return []


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
