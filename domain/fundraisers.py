from pydantic import BaseModel
from typing import Optional


class Fundraiser(BaseModel):
    id: Optional[int]
    name: str
    description:str
    address: str
    city: str
    state: str
    zip: str
    date_start: str
    date_end: str


class UserFundraiserEnrollment(BaseModel):
    user_id: int
    fundraiser_id: int
    fundraiser_goal_amount: int