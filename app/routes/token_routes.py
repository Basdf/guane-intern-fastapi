from fastapi import APIRouter, Body, Depends, Response

from app.models.token_model import (
    TokenModel,
    TokenRespose,
)
from app.services.jwt_service import post_token_service

router = APIRouter()


@router.post(
    "/",
    name="Post Token",
    response_description="Token created",
    response_model=TokenRespose,
)
async def post_token(res: Response, data: TokenModel = Body(...)):
    token_response = await post_token_service(data.dict())
    res.status_code = token_response.code
    return token_response
