import bson
from typing import List

from configs.db import db
from models.car import Car
from utils.utils import make_proj_dict, get_page_metadata


async def get_car_by_id_service(id: str):
    """Метод для получения машины из БД по id
    id: ID машины из БД"""
    result = db['car'].find_one({'_id': bson.ObjectId})
    result['_id'] = str(result['_id'])
    return {
        'message': 'success',
        'car': result
    }


async def get_car_by_name_service(name: str):
    """Метод для получения машины из БД по имени
    name: имя машины (product_name в БД)"""
    result = db['car'].find_one({'product_name': name})
    result['_id'] = str(result['_id'])
    return {
        'message': 'success',
        'car': result
    }


async def get_all_cars_service(page_number: int, page_limit: int):
    """Получение страницы с машинами (по запросу на получение всех машин)
    page_number: номер страницы
    page_limit: количество элементов на странице"""
    skip, pages_count = get_page_metadata(page_number, page_limit, db['car'].count())
    result_cursor = db['car'].find().skip(skip).limit(page_limit)

    result = []
    for i, car in enumerate(result_cursor):
        car['_id'] = str(car['_id'])
        result.append(car)

    return {
        'message': 'success',
        'info': {
            'page_number': page_number,
            'results_per_page': page_limit,
            'pages_count': pages_count
        },
        'result': result
    }


async def get_car_projection_service(car_id: str, projection: List[str]):
    """Метод для получения информации о машине с определенной проекцией
    car_id: ID машины
    projection: список полей БД, которые необходимо вернуть"""
    proj = make_proj_dict(projection)

    result = db['car'].find_one({'_id': bson.ObjectId(car_id)}, projection=proj)
    result['_id'] = str(result['_id'])

    return {
        'message': 'success',
        'result': result
    }


async def get_cars_projection_service(page_number: int, page_limit: int, projection: List[str]):
    """Метод для получения информации о машинах с определенной проекцией
    page_number: номер страницы
    page_limit: количество элементов на странице
    projection: список полей БД, которые необходимо вернуть"""
    proj = make_proj_dict(projection)
    skip, pages_count = get_page_metadata(page_number, page_limit, db['car'].count())

    result_cursor = db['car'].find({}, projection=proj).skip(skip).limit(page_limit)
    result = []
    for car in result_cursor:
        car['_id'] = str(car['_id'])
        result.append(car)

    return {
        'message': 'success',
        'result': result
    }


async def add_new_car_service(car: Car):
    """Метод для добавления новой машины в БД
    car: модель машины (в контексте БД)"""
    car_added_result = db['car'].insert_one(car.dict())
    car_added = car.dict()
    car_added['_id'] = str(car_added_result.inserted_id)
    return {
        'message': 'success',
        'car': car_added
    }


async def update_car_service(car_id: str, updated_params: dict):
    """Метод для обновления информации о машине, которая уже есть в БД
    car_id: ID машины в БД
    car: словарь параметров, которые необходимо изменить"""
    db['car'].update_one({'_id': bson.ObjectId(car_id)}, {
        '$set': updated_params
    })

    result = db['car'].find_one({'_id': bson.ObjectId(car_id)})
    result['_id'] = str(result['_id'])
    return {
        'message': 'success',
        'result': result
    }


async def delete_car_service(car_id: str):
    """Метод для удаления машины из БД
    car_id: ID машины из БД"""
    db['car'].delete_one({'_id': bson.ObjectId(car_id)})
    return {
        'message': 'success'
    }
