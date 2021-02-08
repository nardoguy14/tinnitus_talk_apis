from fastapi import APIRouter
from typing import Optional
from domain.user import User
from services import users_service

router = APIRouter()

@router.post("/users")
async def create_user(user: User):
    return users_service.create_user(user)
