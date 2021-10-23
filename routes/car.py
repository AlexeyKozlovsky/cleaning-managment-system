from fastapi import APIRouter, Query

from models.car import Car
from services.car import add_new_car_service, get_car_by_id_service, get_car_by_name_service, get_all_cars_service

car_router = APIRouter(prefix='/cars')


@car_router.post('/add')
async def add_new_car(car: Car):
    return await add_new_car_service(car)


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
