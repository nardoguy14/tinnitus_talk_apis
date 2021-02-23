from pydantic import BaseModel
from typing import Optional

class Donation(BaseModel):
    user_id: int
    fundraiser_id: str
    donor_first_name: Optional[str]
    donor_last_name: Optional[str]
    donor_comment: Optional[str]
    amount: int
    currency: str
