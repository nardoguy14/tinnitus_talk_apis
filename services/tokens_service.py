import jwt
from domain.user import User

secret = "secret"


def encode_token(user: User):
    encoded_jwt = jwt.encode({"email": user.email,
                              "username": user.username,
                              "id": user.id}, secret, algorithm="HS256")
    return encoded_jwt


def decode_token(token: str):
    return jwt.decode(token, secret, algorithms="HS256")