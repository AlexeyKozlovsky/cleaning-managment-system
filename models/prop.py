from typing import Optional

from pydantic import BaseModel


class Property(BaseModel):
    name: str               # Имя свойства
    weight: float           # Вес свойства
    desc: Optional[str]     # Описание свойства
