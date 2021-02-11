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
    return donations_service.get_donations(username)

