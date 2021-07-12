from pydantic import BaseModel
from typing import Optional, List

from domain.donation import Donation, DonationWithUser


class FundraiserDetails(BaseModel):
    title: str
    detail: str


class FundraiserContact(BaseModel):
    name: str
    phone_number: str
    email: str


class Fundraiser(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]
    editor_details: Optional[str]
    details: Optional[List[FundraiserDetails]]
    address: Optional[str]
    city: Optional[str]
    state: Optional[str]
    zip: Optional[str]
    people: Optional[List[DonationWithUser]]
    contact: Optional[FundraiserContact]
    date_start: Optional[str]
    date_end: Optional[str]


class UserFundraiserEnrollment(BaseModel):
    user_id: int
    fundraiser_id: int
    fundraiser_goal_amount: int
    fundraiser: Optional[Fundraiser]


