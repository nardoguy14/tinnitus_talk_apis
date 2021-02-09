from fastapi import APIRouter
from typing import Optional
from domain.user import User, UserSearch
from services import users_service

router = APIRouter()


@router.post("/users")
async def create_user(user: User):
    return users_service.create_user(user)


@router.get("/users")
async def get_user(first_name: Optional[str] = None, last_name: Optional[str] = None,
                      email: Optional[str] = None, username: Optional[str] = None):
    user_search = UserSearch(first_name=first_name, last_name=last_name,
                             email=email, username=username)
    return users_service.get_user(user_search)
