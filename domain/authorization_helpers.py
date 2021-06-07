from fastapi import Request, HTTPException, status
from services.tokens_service import decode_token
import logging

logger = logging.getLogger()

async def authorization_check(request: Request):
    try:
        bearer_token = request.headers['Authorization'].split(' ')[1]
        users_params = decode_token(bearer_token)
        return users_params
    except Exception as e:
        logger.error(e)
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Not authorized to access endpoint.")