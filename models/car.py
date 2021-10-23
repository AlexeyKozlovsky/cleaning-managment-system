from datetime import datetime
from typing import List

from pydantic import BaseModel


class AdditionalCarInfo(BaseModel):
    manufacture_country: str            # Страна производителя
    manufacture_name: str               # Имя производителя
    manufacture_legal_address: str      # Юридический адрес
    trademark: str                      # Торговая марка
    dimensions: List[int]               # Габаритные размеры
    manufacture_date: datetime          # Дата производства
    batch_number: str                   # Серийный номер
    GOST: str                           # гост
    guarantee_period: datetime          # Гарантийный период


class FuelEstimation(BaseModel):
    km: float       # Среднее количество километров для проезда на одном полном баке бензина
    km_error: float # Погрешность по количеству килмотров для проезда на одном баке (в километрах)
    hour: float     # Среднее количество часов для езды на одном баке
    hour_error: float # Погрешность по количеству часов для езды на одном баке (в часах)


class CarStatuses(BaseModel):
    is_working: bool        # Простаивает или работает машина
    in_repair: bool         # В починке ли машина


class CarJob(BaseModel):
    job_name: str


class Car(BaseModel):
    product_name: str
    statuses: CarStatuses
    additional_info: AdditionalCarInfo
    fuel_estimation: FuelEstimation
    car_job: CarJob
