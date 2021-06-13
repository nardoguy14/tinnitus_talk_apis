from fastapi import HTTPException, UploadFile
from domain.user import User, UserSearch
from repository import users_repository
from services import password_service, tokens_service
from services import aws_service

def create_user(user: User):
    plain_password = user.password
    user.password = password_service.hash_password(user.password)
    users_repository.create_user(user)
    return login_user(user.username, plain_password)


def login_user(user_name: str, password: str):
    users_opt = users_repository.get_password_hash(user_name)
    if len(users_opt) == 0:
        raise HTTPException(400, "User does not exist")
    password_hash = users_opt[0]
    print(password_hash)
    if password_service.check_password(password, password_hash):
        user = get_user(UserSearch(username= user_name))[0]
        access_token = tokens_service.encode_token(user)
        return {
            "access_token": access_token
        }
    else:
        raise HTTPException(400, "Invalid credentials.")


def update_user(user_claims, user: User):
    if user.password:
        user.password = password_service.hash_password(user.password)
    return users_repository.update_user(user_claims, user)


def get_user(user_search: UserSearch):
    return users_repository.get_user(user_search)


def upload_photo(photo_kind: str, username: str, file: UploadFile):
    aws_service.upload_file(username, f'{photo_kind}photo.jpg', file, "tinnitus-app")


def download_photo(photo_kind: str, username: str):
    return aws_service.download_file(username, "tinnitus-app", f"{photo_kind}photo.jpg")
