from typing import Optional

from pydantic import BaseModel


class Param(BaseModel):
    param_name: str
    param_value: object
    desc: Optional[str]
