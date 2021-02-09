from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    first_name: str
    last_name:str
    description: str
    email: str
    username: str
    password: Optional[str]


class UserSearch(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    username: Optional[str]