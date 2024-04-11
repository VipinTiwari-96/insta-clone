from fastapi import APIRouter, Depends;
from sqlalchemy.orm import Session;

# schemas
from ..schemas.post import PostResponse, PostCreate;
# db
from ..get_db import get_db;
# services
from ..services import post as postService


router= APIRouter(
        tags=['Posts']
)



@router.get('/posts', response_model= list[PostResponse])
def get_posts(db:Session= Depends(get_db) ):
    return postService.get_posts(db)


@router.get('/posts/{id}', response_model= PostResponse)
def get_post(id: int, db:Session= Depends(get_db) ):
    return postService.get_post(db, id)


@router.post('/posts', response_model= PostResponse)
def create_post(post: PostCreate, db: Session= Depends(get_db) ):
    return postService.create_post(db, post)


@router.delete('/posts/{id}', response_model= str)
def delete_post(post_id: int, db: Session= Depends(get_db) ):
    return postService.delete_post(db)