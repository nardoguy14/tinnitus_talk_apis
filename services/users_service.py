from domain.user import User
from repository import users_repository
from services import password_service

def create_user(user: User):
    user.password = password_service.hash_password(user.password)
    return users_repository.create_user(user)