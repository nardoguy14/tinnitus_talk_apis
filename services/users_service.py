from domain.user import User
from repository import users_repository


def create_user(user: User):
    return users_repository.create_user(user)