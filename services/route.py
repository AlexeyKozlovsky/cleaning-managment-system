import bson

from configs.db import db
from utils.utils import get_paginate_with_projection


async def get_routes_by_point_service(lon: float, lat: float):
    pass


async def get_routes_by_road_service(road_id: str):
    pass


async def get_routes_by_color(hex_color: str):
    pass


async def get_routes_service(page_number: int, page_limit: int):
    return get_paginate_with_projection(page_number, page_limit, [],
                                        db['route'])


async def get_routes_in_points_service(page_number: int, page_limit: int):
    result = get_paginate_with_projection(page_number, page_limit, [], db['route'])

    routes = result['result']
    routes_points = []
    for i, route in enumerate(routes):
        route_points = []
        for road_id in route['road_ids']:
            road = db['road'].find_one({'_id': bson.ObjectId(road_id)})
            in_point = road['in_vertics']['coordinates']
            out_point = road['out_vertics']['coordinates']

            route_points.append(in_point)

        routes_points.append({
            'hex_color': routes[i]['color_hex'],
            'points': route_points,
            'car_ids': routes[i]['car_ids']
        })

    return {
        'message': 'success',
        'result': routes_points
    }

