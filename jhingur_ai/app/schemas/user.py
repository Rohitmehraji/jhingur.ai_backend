from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema for user creation
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Schema for reading/returning user data
class User(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        from_attributes = True

# Schema for updating user data
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None

# Schema for token data
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[EmailStr] = None
