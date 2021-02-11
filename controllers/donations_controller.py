from fastapi import APIRouter
from typing import Optional
from domain.donation import Donation
from services import donations_service

donations_router = APIRouter()


@donations_router.post("/donations")
async def create_donation(donation: Donation):
    return donations_service.create_donation(donation)

@donations_router.get("/users/donations")
async def get_donation(username: str):
    return donations_service.get_donations(username=username, fundraiser_id=None)

@donations_router.get("/donations/fundraiser/{fundraiser_id}")
async def get_donation(fundraiser_id: str):
    return donations_service.get_donations(username=None, fundraiser_id=fundraiser_id)

