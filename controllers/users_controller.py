from fastapi import APIRouter, Form, Request, Header, HTTPException
from typing import Optional
from domain.user import User, UserSearch
from services import users_service

router = APIRouter()

@router.post("/users/me/login")
async def update_user(username: str = Form(...),
                      password: str = Form(...),
                      grant_type: Optional[str] = Header(None)):
    if grant_type != "password":
        return HTTPException(409, "Grant type not provided.")
    return users_service.login_user(username, password)


@router.post("/users")
async def create_user(user: User):
    return users_service.create_user(user)


@router.put("/users")
async def update_user(user: User):
    return users_service.update_user(user)


@router.get("/users")
async def get_user(first_name: Optional[str] = None, last_name: Optional[str] = None,
                      email: Optional[str] = None, username: Optional[str] = None):
    user_search = UserSearch(first_name=first_name, last_name=last_name,
                             email=email, username=username)
    return users_service.get_user(user_search)
