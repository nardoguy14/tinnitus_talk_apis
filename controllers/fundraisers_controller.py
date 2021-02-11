from fastapi import APIRouter
from domain.fundraisers import Fundraiser
from services import fundraisers_service

fundraisers_router = APIRouter()


@fundraisers_router.post("/fundraisers")
async def create_fundraiser(fundraiser: Fundraiser):
    return fundraisers_service.create_fundraiser(fundraiser)
