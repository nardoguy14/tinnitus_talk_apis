from pydantic import BaseModel
from typing import Optional, List


class Schedule(BaseModel):
    id: Optional[int]
    admin_id: int
    date: str
    start_time: str
    end_time: str
    created_at: Optional[str]
    modified_at: Optional[str]