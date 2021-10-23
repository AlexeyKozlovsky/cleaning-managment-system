import bson
from typing import List

from configs.db import db
from models.car import Car
from utils.utils import get_paginate_with_projection, get_obj_with_projection, update_obj


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
    return get_paginate_with_projection(page_number, page_limit, [], db['car'])


async def get_car_projection_service(car_id: str, projection: List[str]):
    """Метод для получения информации о машине с определенной проекцией
    car_id: ID машины
    projection: список полей БД, которые необходимо вернуть"""
    return get_obj_with_projection(car_id, projection, db['car'])


async def get_cars_projection_service(page_number: int, page_limit: int, projection: List[str]):
    """Метод для получения информации о машинах с определенной проекцией
    page_number: номер страницы
    page_limit: количество элементов на странице
    projection: список полей БД, которые необходимо вернуть"""
    return get_paginate_with_projection(page_number, page_limit, projection, db['car'])


async def add_new_car_service(car: Car):
    """Метод для добавления новой машины в БД
    car: модель машины (в контексте БД)"""
    car_added_result = db['car'].insert_one(car.dict())
    car_added = car.dict()
    car_added['_id'] = str(car_added_result.inserted_id)
    print(car_added)
    return {
        'message': 'success',
        'car': car_added
    }


async def update_car_service(car_id: str, updated_params: dict):
    """Метод для обновления информации о машине, которая уже есть в БД
    car_id: ID машины в БД
    car: словарь параметров, которые необходимо изменить"""
    return update_obj(car_id, updated_params, db['car'])


async def delete_car_service(car_id: str):
    """Метод для удаления машины из БД
    car_id: ID машины из БД"""
    db['car'].delete_one({'_id': bson.ObjectId(car_id)})
    return {
        'message': 'success'
    }
