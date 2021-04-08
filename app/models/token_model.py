from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class TokenModel(BaseModel):
    user: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "user": "eduardo.velasquez",
                "email": "eduardo.velasquez@email.com",
            }
        }


class TokenRespose(BaseModel):
    token: str = Field(...)
    code: int = 200
    message: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "token": "Token Here",
                "code": 200,
                "message": "Token Generate",
            }
        }
