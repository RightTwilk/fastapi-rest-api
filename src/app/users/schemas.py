from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class UserSchema(BaseModel):
    username: str = Field(..., max_length=50)
    email: EmailStr = Field(...)
    full_name: Optional[str] = Field(max_length=50)
    password: str = Field(...)
