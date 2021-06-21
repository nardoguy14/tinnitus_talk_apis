from pydantic import BaseModel
from typing import Optional
from domain.user import User


class Donation(BaseModel):
    user_id: Optional[int]
    username: Optional[str]
    fundraiser_id: str
    donor_first_name: Optional[str]
    donor_last_name: Optional[str]
    donor_comment: Optional[str]
    amount: int
    currency: str


class DonationWithUser(BaseModel):
    user: User
    fundraiser_id: str
    donor_first_name: Optional[str]
    donor_last_name: Optional[str]
    donor_comment: Optional[str]
    amount: int
    currency: str
