from pydantic import BaseModel
from typing import Optional, List

from domain.donation import Donation


class FundraiserDetails(BaseModel):
    title: str
    detail: str


class UserFundraiserEnrollment(BaseModel):
    user_id: int
    fundraiser_id: int
    fundraiser_goal_amount: int


class Fundraiser(BaseModel):
    id: Optional[int]
    name: str
    description:str
    details: Optional[List[FundraiserDetails]]
    address: str
    city: str
    state: str
    zip: str
    people: Optional[List[Donation]]
    date_start: str
    date_end: str
