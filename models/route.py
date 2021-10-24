from typing import List

import bson
from pydantic import BaseModel

from models.road import Road


class Route(BaseModel):
    road_ids: List[str]                       # Список дорог в маршруте
    car_ids: List[str]     # ID машин, которые едут по текущему маршруту
