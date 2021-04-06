from fastapi import APIRouter, Body, Depends
from fastapi.encoders import jsonable_encoder

from app.db.dog_db import (
    add_dog,
    delete_dog,
    retrieve_dog_by_is_adopted,
    retrieve_dog_by_name,
    retrieve_dogs,
    update_dog,
)
from app.models.dog_model import (
    DogModel,
    UpdateDogModel,
    DogResponse,
)
from app.models.response_model import response_model, error_response_model
from app.services import dog_service

router = APIRouter()


@router.get(
    "/",
    response_description="Dogs retrieved",
    response_model=DogResponse,
)
async def get_dogs():
    dogs = await retrieve_dogs()
    if dogs:
        return response_model(dogs, "Dogs data retrieved successfully")
    return response_model(dogs, "Empty list returned")


@router.get(
    "/is_adopted",
    response_description="Dogs adopted retrieved",
    response_model=DogResponse,
)
async def get_dogs_is_adopted():
    dogs = await retrieve_dog_by_is_adopted()
    if dogs:
        return response_model(dogs, "dogs adopted retrieved successfully")
    return response_model(dogs, "Empty list returned")


@router.get(
    "/{name}",
    response_description="Dog data retrieved",
    response_model=DogResponse,
)
async def get_dog_by_name(name: str):
    dog = await retrieve_dog_by_name(name)
    if dog:
        return response_model(dog, "dog data retrieved successfully")
    return error_response_model("An error occurred", 404, "dog doesn't exist")


@router.post(
    "/{name}",
    response_description="Dog data added into the database",
    response_model=DogResponse,
)
async def add_dog_data(name: str):
    dog_data = await dog_service.create_dog_data()
    dog: DogModel = DogModel(
        name=name,
        picture=dog_data["picture"],
        create_date=dog_data["create_date"],
    )

    dog = jsonable_encoder(dog)
    new_dog = await add_dog(dog)

    if new_dog:
        return response_model(new_dog, "dog added successfully.")
    return error_response_model("An error occurred", 404, "repeated name")


@router.put(
    "/{name}",
    response_description="Dog data updated into the database",
)
async def update_dog_data(name: str, req: UpdateDogModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    dog = await update_dog(name, req)

    if dog:
        return response_model(
            f"Dog with Name: {name}, update is successful",
            "Dog updated successfully",
        )
    return error_response_model(
        "An error occurred",
        404,
        "There was an error updating the dog data.",
    )


@router.delete(
    "/{name}",
    response_description="Dog data deleted from the database",
)
async def delete_dog_data(name: str):
    deleted_dog = await delete_dog(name)
    if deleted_dog:
        return response_model(
            f"Dog with name: {name} removed", "dog deleted successfully"
        )
    return error_response_model(
        "An error occurred", 404, f"Dog with name {name} doesn't exist"
    )
