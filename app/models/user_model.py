from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class UserModel(BaseModel):
    id: str = Field(...)
    name: str = Field(...)
    last_name: Optional[str] = None
    email: EmailStr = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "id": "1",
                "name": "Eduardo",
                "last_name": "Velasquez",
                "email": "eduardo.velasquez@email.com",
            }
        }


class UpdateUserModel(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]

    class Config:
        schema_extra = {
            "example": {
                "name": "Eduardo",
                "last_name": "Velasquez",
                "email": "eduardo.velasquez@email.com",
            }
        }


class UserResponse(BaseModel):
    data: list = []
    code: int = 200
    message: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "data": [
                    {
                        "id": "1",
                        "name": "Eduardo",
                        "last_name": "Velasquez",
                        "email": "eduardo.velasquez@email.com",
                    }
                ],
                "code": 200,
                "message": "related message",
            }
        }


class UserErrorResponse(BaseModel):
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
