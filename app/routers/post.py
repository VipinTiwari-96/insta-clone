from fastapi import APIRouter;
# schemas
from ..schemas.post import PostResponse;


router= APIRouter(
        tags=['Posts']
)


@router.get('/posts', response_model= list[PostResponse])
def get_posts():
    return []

@router.get('/posts/{post_id}', response_model= PostResponse)
def get_post(post_id: int):
    return {}


@router.post('/posts', response_model= PostResponse)
def create_post():
    return {}

@router.delete('/posts/{post_id}', response_model= str)
def delete_post(post_id: int):
    return 'success'