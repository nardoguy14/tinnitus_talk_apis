from fastapi import APIRouter
from domain.fundraisers import Fundraiser, UserFundraiserEnrollment
from services import fundraisers_service
from typing import Optional

fundraisers_router = APIRouter()


@fundraisers_router.post("/fundraisers")
async def create_fundraiser(fundraiser: Fundraiser):
    return fundraisers_service.create_fundraiser(fundraiser)

@fundraisers_router.put("/fundraisers/{id}")
async def update_fundraiser(id: str, fundraiser: Fundraiser):
    fundraiser.id = int(id)
    return fundraisers_service.update_fundraiser(fundraiser)

@fundraisers_router.get("/fundraisers")
async def get_all_fundraiser(id: Optional[str], name: Optional[str] = None):
    return fundraisers_service.get_fundraiser(id, name)

@fundraisers_router.post("/users/fundraisers")
async def create_fundraiser(user_fundraiser_enrollment: UserFundraiserEnrollment):
    return fundraisers_service.enroll_user_to_fundraiser(user_fundraiser_enrollment)

@fundraisers_router.get("/users/{user_id}/fundraisers")
async def get_fundraiser(user_id: str):
    return fundraisers_service.get_users_fundraisers(user_id)
