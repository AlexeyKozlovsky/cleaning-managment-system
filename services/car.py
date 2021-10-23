import bson
from typing import List

from configs.db import db
from models.car import Car


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
    pages_count = db['car'].count() // page_limit + 1
    skip = page_limit * (page_number - 1)
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
    pass


async def get_cars_projection_service(page_number: int, page_limit: int, projection: List[str]):
    """Метод для получения информации о машинах с определенной проекцией
    page_number: номер страницы
    page_limit: количество элементов на странице
    projection: список полей БД, которые необходимо вернуть"""
    pass


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


async def update_car_service(car_id: str, car: Car):
    """Метод для обновления информации о машине, которая уже есть в БД
    car_id: ID машины в БД
    car: модель машины (в контексте БД)"""
    pass


async def delete_car_service(car_id: str):
    """Метод для удаления машины из БД
    car_id: ID машины из БД"""
    pass
