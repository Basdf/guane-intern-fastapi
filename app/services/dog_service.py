import httpx
from datetime import datetime

from decouple import config

from app.repository.dog_repository import (
    get_dogs_repository,
    get_adopted_dogs_repository,
    get_dog_by_name_repository,
    update_dog_repository,
    delete_dog_repository,
    save_dog_repository,
)
from app.repository.user_repository import get_user_by_id_repository
from app.models.dog_model import (
    DogModel,
    UpdateDogModel,
    DogResponse,
    DogErrorResponse,
)

API_DOG_IMAGE = config("API_DOG_IMAGE")


async def get_dogs_service():
    dogs = await get_dogs_repository()
    if dogs:
        return DogResponse(
            data=dogs,
            message="Dogs data retrieved successfully.",
        )
    return DogResponse(
        data=dogs,
        message="Empty list returned.",
    )


async def get_adopted_dogs_service():
    dogs = await get_adopted_dogs_repository()

    if dogs:
        return DogResponse(
            data=dogs,
            message="Dogs adopted retrieved successfully.",
        )
    return DogResponse(
        data=dogs,
        message="Empty list returned.",
    )


async def get_dog_by_name_service(name: str):
    dog = await get_dog_by_name_repository(name)
    if dog:
        return DogResponse(
            data=[dog],
            message="Dog data retrieved successfully.",
        )
    return DogErrorResponse(
        error="An error occurred.",
        message="Dog doesn't exist.",
    )


async def post_dog_service(name: str):
    try:
        dog: DogModel = DogModel(
            name=name,
            picture=await get_dogpicture_service(),
            create_date=datetime.now().strftime("%Y-%m-%d, %H:%M:%S.%f"),
        )
    except httpx.HTTPStatusError:
        return DogErrorResponse(
            error="An error occurred.",
            message="An error occurred while generating the image.",
        )
    new_dog = await save_dog_repository(dog.dict())

    if new_dog:
        return DogResponse(
            data=[new_dog],
            message="Dog added successfully.",
        )
    return DogErrorResponse(
        error="An error occurred.",
        message="Repeated name.",
    )


async def put_dog_service(name: str, req: UpdateDogModel):
    req = {k: v for k, v in req.dict().items() if v is not None}

    if "id_user" in req:
        user = await get_user_by_id_repository(req["id_user"])
        if not user:
            return DogErrorResponse(
                error="An error occurred.",
                message="User doesn't exist.",
            )

    dog = await update_dog_repository(name, req)
    if dog:
        return DogResponse(
            data=[dog],
            message="Dog updated successfully.",
        )
    return DogErrorResponse(
        error="An error occurred.",
        message="There was an error updating the dog data.",
    )


async def delete_dog_service(name: str):
    deleted_dog = await delete_dog_repository(name)
    if deleted_dog:
        return DogResponse(
            data=[deleted_dog],
            message="Dog deleted successfully.",
        )
    return DogErrorResponse(
        error="An error occurred.",
        message="Dog doesn't exist.",
    )


async def get_dogpicture_service():
    async with httpx.AsyncClient() as client:
        resp = await client.get(API_DOG_IMAGE)
        resp.raise_for_status()

    data = resp.json()
    return data["message"]
