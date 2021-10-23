from typing import List

import bson
from fastapi import Query

from configs.db import db
from models.prop import Property
from utils.utils import get_obj_with_projection, get_paginate_with_projection, update_obj


async def get_prop_by_id_service(id: str):
    """Метод для получения информации о свойстве из БД по ID
    id: ID свойства из БД"""
    pass


async def get_prop_by_name_service(name: str):
    """Метод для получения информации о свойстве из БД по названию
    name: название свойства"""
    pass


async def get_prop_by_id(id: str, projection: List[str]):
    return get_obj_with_projection(id, projection, db['prop'])


async def get_props_service(page_number: int, page_limit: int):
    """Метод для получения информации о свойствах из БД
    page_number: номер страницы
    page_limit: количество элементов на странице"""
    return get_paginate_with_projection(page_number, page_limit,
                                        [], db['prop'])


async def add_new_prop_service(prop: Property):
    """Метод для добавления нового свойства в БД
    prop: модель свойства (в контексте БД)"""
    prop_added_result = db['prop'].insert_one(prop.dict())
    prop_added = prop.dict()
    prop_added['_id'] = str(prop_added_result.inserted_id)
    print(prop_added)
    return {
        'message': 'success',
        'car': prop_added
    }


async def update_prop_service(prop_id: str, updated_params: dict):
    """Метод для обновления информации о свойстве, которое уже есть в БД
    prop_id: ID свойства из БД
    prop: модель свойства (в контексте БД)"""
    return update_obj(prop_id, updated_params, db['prop'])


async def update_precipitation_level(percentage: float = Query(gt=0, le=1, default=0.5)):
    precipitation_min = db['param'].find_one({'prop_name': 'precipitation_min'})['param_value']
    precipitation_max = db['param'].find_one({'prop_name': 'precipitation_max'})['param_value']
    precipitation_range_len = (precipitation_max - precipitation_min)
    result = precipitation_min + precipitation_range_len * percentage

    # db['prop'].update_one({'prop_name': 'precipitation'}, {
    #     '$set':
    # })


async def delete_prop_service(prop_id: str):
    """Метод для удаления свойства из БД
    prop_id: ID свойства из БД"""
    db['prop'].delete_one({'_id': bson.ObjectId(prop_id)})
    return {
        'message': 'success'
    }
