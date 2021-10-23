from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


renderer = APIRouter()
templates = Jinja2Templates(directory='templates')


@renderer.get('/', include_in_schema=False, response_class=HTMLResponse)
async def render_main_page(req: Request):
    return templates.TemplateResponse('pages/dispatcher.html', {'request': req})


@renderer.get('/add-param', include_in_schema=False, response_class=HTMLResponse)
async def render_add_param_page(req: Request):
    return templates.TemplateResponse('pages/addparam.html', {'request': req})


@renderer.get('/add-weights', include_in_schema=False, response_class=HTMLResponse)
async def render_add_weights_page(req: Request):
    return templates.TemplateResponse('pages/addweights.html', {'request': req})


@renderer.get('/authorize', include_in_schema=False, response_class=HTMLResponse)
async def render_authorized_page(req: Request):
    return templates.TemplateResponse('pages/authorized.html', {'request': req})


@renderer.get('/main', include_in_schema=False, response_class=HTMLResponse)
async def render_main_page(req: Request):
    return templates.TemplateResponse('pages/index.html', {'request': req})


@renderer.get('/correct-param', include_in_schema=False, response_class=HTMLResponse)
async def render_correct_param_page(req: Request):
    return templates.TemplateResponse('pages/correct_param.html', {'request': req})


@renderer.get('/correct-weights', include_in_schema=False, response_class=HTMLResponse)
async def render_correct_weights_page(req: Request):
    return templates.TemplateResponse('pages/correct_weights.html', {'request': req})


@renderer.get('/add-car', include_in_schema=False, response_class=HTMLResponse)
async def render_add_car_page(req: Request):
    return templates.TemplateResponse('pages/addcar.html', {'request': req})


@renderer.get('/dispatcher-page', include_in_schema=False, response_class=HTMLResponse)
async def render_dispatcher_page(req: Request):
    return templates.TemplateResponse('pages/dispatcher-page.html', {'request': req})