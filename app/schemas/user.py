from pydantic import BaseModel;
from datetime import datetime;

class UserBase(BaseModel):
    user_name: str
    age: int



class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime