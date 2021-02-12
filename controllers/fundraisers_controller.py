from fastapi import APIRouter
from domain.fundraisers import Fundraiser
from services import fundraisers_service
from typing import Optional

fundraisers_router = APIRouter()


@fundraisers_router.post("/fundraisers")
async def create_fundraiser(fundraiser: Fundraiser):
    return fundraisers_service.create_fundraiser(fundraiser)

@fundraisers_router.put("/fundraisers/{id}")
async def create_fundraiser(id: str, fundraiser: Fundraiser):
    fundraiser.id = int(id)
    return fundraisers_service.update_fundraiser(fundraiser)

@fundraisers_router.get("/fundraisers")
async def create_fundraiser(id: Optional[str], name: Optional[str] = None):
    return fundraisers_service.get_fundraiser(id, name)
