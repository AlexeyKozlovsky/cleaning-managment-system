import bson

from configs.db import db
from models.car import Car


async def add_new_car_service(car: Car):
    car_added_result = db['car'].insert_one(car.dict())
    car_added = car.dict()
    car_added['_id'] = str(car_added_result.inserted_id)
    return {
        'message': 'success',
        'car': car_added
    }


async def get_car_by_id_service(id: str):
    result = db['car'].find_one({'_id': bson.ObjectId})
    result['_id'] = str(result['_id'])
    return {
        'message': 'success',
        'car': result
    }


async def get_car_by_name_service(name: str):
    result = db['car'].find_one({'product_name': name})
    result['_id'] = str(result['_id'])
    return {
        'message': 'success',
        'car': result
    }
