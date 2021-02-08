from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    first_name: str
    last_name:str
    description: str
    email: str
    username: str
    password: Optional[str]