from typing import List

from fastapi import APIRouter, Query

from models.car import Car
from services.car import add_new_car_service, get_car_by_id_service, get_car_by_name_service, get_all_cars_service, \
    get_car_projection_service, get_cars_projection_service, update_car_service, delete_car_service

car_router = APIRouter(prefix='/cars')


@car_router.get('/{id}')
async def get_car_by_id(id: str):
    return await get_car_by_id_service(id)


@car_router.get('/by-name')
async def get_car_by_name(name: str):
    return await get_car_by_name_service(name)


@car_router.get('/')
async def get_all_cars(page_number: int = Query(gt=0, default=1),
                       page_limit: int = Query(gt=0, le=25, default=10)):
    return await get_all_cars_service(page_number, page_limit)


@car_router.post('/{id}')
async def get_car_projection(car_id: str, projection: List[str]):
    return await get_car_projection_service(car_id, projection)


@car_router.post('/')
async def get_cars_projection(page_number: int = Query(gt=0, default=1),
                              page_limit: int = Query(gt=0, le=25, default=10),
                              projection: List[str] = Query(default=[])):
    return await get_cars_projection_service(page_number, page_limit, projection)


@car_router.post('/add/')
async def add_new_car(car: Car):
    print(car)
    return await add_new_car_service(car)


@car_router.put('/update/{id}')
async def update_car(id: str, updated_params: dict):
    return await update_car_service(id, updated_params)


@car_router.delete('/delete/{id}')
async def delete_car(id: str):
    return await delete_car_service(id)
