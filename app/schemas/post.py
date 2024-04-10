from pydantic import BaseModel;
from typing import Optional;


class PostBase(BaseModel):
   title: str
   content: Optional[str]= None
   is_published: bool



class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: str
    updated_at: str