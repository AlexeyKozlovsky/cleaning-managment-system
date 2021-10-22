from fastapi import FastAPI

from routes.car import car_router
from routes.route import route_router
from routes.prop import prop_router
from routes.graph import graph_router


app = FastAPI()
app.include_router(car_router)
app.include_router(route_router)
app.include_router(prop_router)
app.include_router(graph_router)


@app.get('/')
async def main_page():
    return {
        'message': 'tilt'
    }
