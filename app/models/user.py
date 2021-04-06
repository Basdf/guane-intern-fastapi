from typing import Optional
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: str = Field(...)
    name: str = Field(...)
    last_name: Optional[str] = None
    email: EmailStr = Field(...)
