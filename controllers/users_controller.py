from fastapi import APIRouter, Form, UploadFile, File, Header, HTTPException, Depends
from typing import Optional
import io
from starlette.responses import StreamingResponse

from domain.user import User, UserSearch, UserPhoto
from services import users_service
from domain.authorization_helpers import authorization_check
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

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


@router.post("/users/photos/{photo_kind}/base64")
async def upload_profile_photo2(photo_kind: str, photo: UserPhoto, user_claims=Depends(authorization_check)):
    await users_service.upload_photo(photo_kind, user_claims['username'], photo.base64photo)
    return {"filename": "done"}


@router.get("/users/{username}/photos/{photo_kind}")
def image_endpoint2(username: str, photo_kind: str):
    file = users_service.download_photo(photo_kind, username)
    return {'file': file}
    # return StreamingResponse(io.BytesIO(file), media_type="image/jpg")

@router.get("/users/photos/{photo_kind}")
def image_endpoint(photo_kind: str, user_claims=Depends(authorization_check)):
    file = users_service.download_photo(photo_kind, user_claims['username'])
    return {'file': file}
    # return StreamingResponse(io.BytesIO(file), media_type="image/jpg")


@router.put("/users")
async def update_user(user: User, user_claims=Depends(authorization_check)):
    return users_service.update_user(user_claims, user)


@router.get("/users")
async def get_user(first_name: Optional[str] = None, last_name: Optional[str] = None,
                      email: Optional[str] = None, username: Optional[str] = None):
    user_search = UserSearch(first_name=first_name, last_name=last_name,
                             email=email, username=username)
    return users_service.get_user(user_search)
