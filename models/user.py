import datetime
from typing import List

from pydantic import BaseModel

from models.route import Route


class User(BaseModel):
    username: str
    email: str
    password_hash: str


class Driver(User):
    working_hours: List[datetime.time]
    working_days: List[datetime.date]
    is_working: bool


class Citizen(User):
    requested_routes: List[Route]
