from fastapi import APIRouter
from typing import Optional
from domain.activity import Activity
from domain.user import User, UserSearch
from services import activities_service

activities_router = APIRouter()


@activities_router.post("/activities")
async def update_user(activity: Activity):
    return activities_service.create_activity(activity)


@activities_router.get("/activities")
async def get_user(fundraiser_id: int):
    return activities_service.get_activities(fundraiser_id)
