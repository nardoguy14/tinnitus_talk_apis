from pydantic import BaseModel
from typing import Optional

class Donation(BaseModel):
    username: str
    donor_first_name: str
    donor_last_name: str
    donor_comment: str
    fundraiser_id: str
    amount: int
    currency: str
