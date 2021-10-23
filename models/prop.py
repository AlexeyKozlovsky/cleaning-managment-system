from typing import Optional

from pydantic import BaseModel


class Property(BaseModel):
    name: str               # Имя свойства на русском (для отображения)
    prop_name: str          # Имя свойства для обращения
    weight: float           # Вес свойства
    desc: Optional[str]     # Описание свойства
