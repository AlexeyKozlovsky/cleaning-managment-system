from typing import List

import bson
from pydantic import BaseModel

from models.road import Road


class Route(BaseModel):
    roads: List[Road]                       # Список дорог в маршруте
    actual_car_ids: List[bson.ObjectId]     # ID машин, которые едут по текущему маршруту
