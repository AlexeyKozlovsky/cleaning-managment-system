from fastapi import APIRouter

from models.car import Car
from services.car import add_new_car_service, get_car_by_id_service, get_car_by_name_service

car_router = APIRouter(prefix='/cars')


@car_router.post('/add')
async def add_new_car(car: Car):
    return await add_new_car_service(car)


@car_router.get('/{id}')
async def get_car_by_id(id: str):
    return await get_car_by_id_service(id)


@car_router.get('/')
async def get_car_by_name(name: str):
    return await get_car_by_name_service(name)
