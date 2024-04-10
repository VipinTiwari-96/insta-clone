from pydantic import BaseModel;


class UserBase(BaseModel):
    user_name: str
    age: int



class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id: int
    created_at: str
    updated_at: str