from pydantic import BaseModel
from typing import Optional, List

from domain.donation import Donation, DonationWithUser


class Activity(BaseModel):
    fundraiser_id: int
    distance: float
    activity_type: str
    date_start: str
    created_at: str