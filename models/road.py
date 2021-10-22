from typing import List

import bson
from pydantic import BaseModel


class Road(BaseModel):
    weight: float                   # Вес текущей дороги в графе
    in_vertics_id: bson.ObjectId    # ID начальной вершины
    out_vertics_id: bson.ObjectId   # ID конечной вершины
    speed_limit: int                # Ограничение по скорости
