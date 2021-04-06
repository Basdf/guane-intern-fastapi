from typing import Optional
from pydantic import BaseModel, Field


class DogModel(BaseModel):
    id_user: str = None
    name: str = Field(...)
    picture: str = Field(...)
    create_date: str = Field(...)
    is_adopted: bool = False


class UpdateDogModel(BaseModel):
    id_user: Optional[str]
    name: Optional[str]
    picture: Optional[str]
    create_date: Optional[str]
    is_adopted: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "id": "1",
                "id_user": "15254",
                "name": "firulais",
                "picture": "https://images.dog.ceo/breeds/shiba/shiba.jpg",
                "create_date": "05/04/2021",
                "is_adopted": True,
            }
        }


class DogResponse(BaseModel):
    data: list = []
    code: int = 200
    message: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "data": {
                    "id": "1",
                    "id_user": "15254",
                    "name": "firulais",
                    "picture": "https://images.dog.ceo/breeds/shiba/shiba.jpg",
                    "create_date": "05/04/2021",
                    "is_adopted": True,
                },
                "code": 200,
                "message": "related message",
            }
        }
