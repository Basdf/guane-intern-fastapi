from fastapi import APIRouter, Body, Response, Depends
from fastapi.encoders import jsonable_encoder

from app.services import user_service
from app.models.user_model import (
    UserModel,
    UpdateUserModel,
    UserResponse,
    UserErrorResponse,
)
from app.services.jwt_service import verify_token

PROTECTED = [Depends(verify_token)]

router = APIRouter()


@router.get(
    "/",
    name="Get all Users",
    response_description="Users retrieved",
    response_model=UserResponse,
)
async def get_users(res: Response):
    user_response = await user_service.get_users_service()
    res.status_code = user_response.code
    return user_response


@router.get(
    "/{id}",
    name="Get User by ID",
    response_description="User data retrieved",
    response_model=UserResponse,
    responses={400: {"model": UserErrorResponse}},
)
async def get_user_by_id(id: str, res: Response):
    user_response = await user_service.get_user_by_id_service(id)
    res.status_code = user_response.code
    return user_response


@router.post(
    "/",
    name="Post User",
    response_description="User data added into the database",
    response_model=UserResponse,
    responses={400: {"model": UserErrorResponse}},
    dependencies=PROTECTED,
)
async def post_user(res: Response, user: UserModel = Body(...)):
    user_response = await user_service.post_user_service(user)
    res.status_code = user_response.code
    return user_response


@router.put(
    "/{id}",
    name="Put User",
    response_description="User data updated into the database",
    response_model=UserResponse,
    responses={400: {"model": UserErrorResponse}},
)
async def put_user(id: str, res: Response, req: UpdateUserModel = Body(...)):
    user_response = await user_service.put_user_service(id, req)
    res.status_code = user_response.code
    return user_response


@router.delete(
    "/{id}",
    name="Delete User",
    response_description="User data deleted from the database",
    response_model=UserResponse,
    responses={400: {"model": UserErrorResponse}},
)
async def delete_user(id: str, res: Response):
    user_response = await user_service.delete_user_service(id)
    res.status_code = user_response.code
    return user_response
