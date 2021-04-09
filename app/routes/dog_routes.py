from fastapi import APIRouter, Body, Depends, Response

from app.models.dog_model import (
    DogModel,
    UpdateDogModel,
    DogResponse,
    DogErrorResponse,
)
from app.services import dog_service
from app.services.jwt_service import verify_token

PROTECTED = [Depends(verify_token)]

router = APIRouter()


@router.get(
    "/",
    name="Get all Dogs",
    response_description="Dogs retrieved",
    response_model=DogResponse,
)
async def get_dogs(res: Response):
    dog_response = await dog_service.get_dogs_service()
    res.status_code = dog_response.code
    return dog_response


@router.get(
    "/is_adopted",
    name="Get adopted Dogs",
    response_description="Dogs adopted retrieved",
    response_model=DogResponse,
)
async def get_adopted_dogs(res: Response):
    dog_response = await dog_service.get_adopted_dogs_service()
    res.status_code = dog_response.code
    return dog_response


@router.get(
    "/{name}",
    name="Get Dog by name",
    response_description="Dog data retrieved",
    response_model=DogResponse,
    responses={400: {"model": DogErrorResponse}},
)
async def get_dog_by_name(name: str, res: Response):
    dog_response = await dog_service.get_dog_by_name_service(name)
    res.status_code = dog_response.code
    return dog_response


@router.post(
    "/{name}",
    name="Post Dog",
    response_description="Dog data added into the database",
    response_model=DogResponse,
    responses={400: {"model": DogErrorResponse}},
    dependencies=PROTECTED,
)
async def post_dog(name: str, res: Response):
    dog_response = await dog_service.post_dog_service(name)
    res.status_code = dog_response.code
    return dog_response


@router.put(
    "/{name}",
    name="Update Dog",
    response_description="Dog data updated into the database",
    response_model=DogResponse,
    responses={400: {"model": DogErrorResponse}},
)
async def put_dog(name: str, res: Response, req: UpdateDogModel = Body(...)):
    dog_response = await dog_service.put_dog_service(name, req)
    res.status_code = dog_response.code
    return dog_response


@router.delete(
    "/{name}",
    name="Delete Dog",
    response_description="Dog data deleted from the database",
    response_model=DogResponse,
    responses={400: {"model": DogErrorResponse}},
)
async def delete_dog(name: str, res: Response):
    dog_response = await dog_service.delete_dog_service(name)
    res.status_code = dog_response.code
    return dog_response
