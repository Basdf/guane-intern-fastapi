from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBearer
from jose import jwt
from jose.exceptions import JOSEError
from decouple import config

from app.models.token_model import TokenRespose

SECRET_KEY = config("SECRET_KEY")
ALGORITHM = config("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int)


security = HTTPBearer()


def verify_token(credentials: HTTPBasicCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=ALGORITHM)
    except JOSEError as e:
        raise HTTPException(status_code=401, detail=str(e))


async def post_token_service(data: dict):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"exp": expire})
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return TokenRespose(token=encoded_jwt, message="Generated token")
