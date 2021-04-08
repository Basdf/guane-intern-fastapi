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
    picture: Optional[str]
    create_date: Optional[str]
    is_adopted: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "id_user": "1",
                "picture": "URL HERE",
                "create_date": "2021-04-08, 13:22:30.593272",
                "is_adopted": False,
            }
        }


class DogResponse(BaseModel):
    data: list = []
    code: int = 200
    message: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "data": [
                    {
                        "id": "1",
                        "id_user": "1",
                        "name": "firulais",
                        "picture": "URL HERE",
                        "create_date": "2021-04-08, 13:22:30.593272",
                        "is_adopted": True,
                    }
                ],
                "code": 200,
                "message": "related message",
            }
        }


class DogErrorResponse(BaseModel):
    error: str
    code: int = 400
    message: str

    class Config:
        schema_extra = {
            "example": {
                "error": "Error",
                "code": 400,
                "message": "related message",
            }
        }
