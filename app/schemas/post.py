from pydantic import BaseModel;
from typing import Optional;
from datetime import datetime;

class PostBase(BaseModel):
   title: str
   content: Optional[str]= None
   is_published: bool




class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: datetime