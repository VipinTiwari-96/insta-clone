from pydantic import BaseModel, EmailStr;
from datetime import datetime;
from .post import PostResponse;

class UserBase(BaseModel):
    user_name: EmailStr
    age: int



class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    posts: list[PostResponse]