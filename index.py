from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from routes.car import car_router
from routes.renderer import renderer
from routes.route import route_router
from routes.prop import prop_router
from routes.graph import graph_router


app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory='templates')

origins = ['80.87.111.51:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['GET', 'POST'],
    allow_headers=['*']
)

app.include_router(car_router)
app.include_router(route_router)
app.include_router(prop_router)
app.include_router(graph_router)
app.include_router(renderer)


@app.get('/road_graph', include_in_schema=False, response_class=HTMLResponse)
async def road_graph_page(request: Request):
    return templates.TemplateResponse('graph_map.html', {'request': request})
