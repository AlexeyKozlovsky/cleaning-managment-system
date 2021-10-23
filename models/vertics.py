from typing import List

from pydantic import BaseModel


class Vertics(BaseModel):
    coordinates: List[float]
