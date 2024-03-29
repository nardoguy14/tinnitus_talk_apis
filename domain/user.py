from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: Optional[int]
    firstName: Optional[str]
    lastName: Optional[str]
    description: Optional[str]
    email: Optional[str]
    username: Optional[str]
    password: Optional[str]
    dateOfBirth: Optional[str]
    streetAddress1: Optional[str]
    streetAddress2: Optional[str]
    country: Optional[str]
    zipCode: Optional[str]
    phoneNumber: Optional[str]


class UserPhoto(BaseModel):
    base64photo: str


class UserSearch(BaseModel):
    user_id: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    username: Optional[str]
