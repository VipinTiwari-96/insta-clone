
from pydantic import BaseModel, EmailStr;
from typing import Optional;

class AuthBase(BaseModel):
    user_name: EmailStr
    access_token: str

class TokenData(BaseModel):
    id: Optional[str] = None