from pydantic import BaseModel


class Fundraiser(BaseModel):
    name: str
    description:str
    address: str
    city: str
    state: str
    zip: str
    date_start: str
    date_end: str
