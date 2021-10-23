from fastapi import APIRouter, Query

from models.prop import Property
from services.prop import (get_prop_by_id_service, get_prop_by_name_service,
                           get_props_service, add_new_prop_service, update_prop_service)

prop_router = APIRouter(prefix='/props')


@prop_router.get('/{id}')
async def get_prop_by_id(id: str):
    return await get_prop_by_id_service(id)


@prop_router.get('/')
async def get_prop_by_name(name: str):
    return await get_prop_by_name_service(name)


@prop_router.get('/all/')
async def get_props(page_number: int = Query(gt=0, default=1),
                    page_limit: int = Query(gt=0, le=25, default=10)):
    return await get_props_service(page_number, page_limit)


@prop_router.post('/')
async def add_new_prop(prop: Property):
    return await add_new_prop_service(prop)


@prop_router.put('/update/{id}')
async def update_prop(id: str, updated_params: dict):
    return await update_prop_service(id, updated_params)


@prop_router.delete('/delete/{id}')
async def delete_prop_service(id: str):
    return await delete_prop_service(id)
