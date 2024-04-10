from pydantic import BaseModel;


class PostBase(BaseModel):
   title: str
   content: str
   is_published: bool



class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: str
    updated_at: str