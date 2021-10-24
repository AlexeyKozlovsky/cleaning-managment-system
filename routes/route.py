from fastapi import APIRouter, Query

from models.route import Route
from services.route import get_routes_by_point_service, get_routes_by_road_service, get_routes_service, \
    get_routes_in_points_service

route_router = APIRouter(prefix='/routes')


@route_router.get('/by-point')
async def get_routes_by_point(lon: float, lat: float):
    return await get_routes_by_point_service(lon, lat)


@route_router.get('/by-road')
async def get_routes_by_road(road_id: str):
    return await get_routes_by_road_service(road_id)


@route_router.get('/by-color')
async def get_routes_by_color(hex_color: str):
    return await get_routes_by_color(hex_color)


@route_router.get('/')
async def get_routes(page_number: int = Query(gt=0, default=1),
                     page_limit: int = Query(gt=0, le=25, default=10)):
    return await get_routes_service(page_number, page_limit)


@route_router.get('/in-points')
async def get_routes_in_points(page_number: int = Query(gt=0, default=1),
                               page_limit: int = Query(gt=0, le=25, default=10)):
    return await get_routes_in_points_service(page_number, page_limit)


@route_router.post('/new')
async def add_new_route(route: Route):
    pass


@route_router.put('/update/{id}')
async def update_route(id: str, updated_params: dict):
    pass


@route_router.delete('/delete/{id}')
async def delete_route(id: str):
    pass
