from fastapi import APIRouter, Depends, HTTPException, status;
from sqlalchemy.orm import Session;

# schemas
from ..schemas.post import PostResponse, PostCreate;
from ..schemas.user import UserResponse;
# db
from ..get_db import get_db;
# services
from ..services import post as postService
from ..oauth2 import get_current_user;

router= APIRouter(
        tags=['Posts']
)



@router.get('/posts', response_model= list[PostResponse])
def get_posts(db:Session= Depends(get_db), current_user:UserResponse= Depends(get_current_user)):
    return postService.get_posts(db, current_user)


@router.get('/posts/{id}', response_model= PostResponse)
def get_post(id: int, db:Session= Depends(get_db), current_user:UserResponse= Depends(get_current_user) ):
    db_post= postService.get_post(db, id, current_user)
    if db_post is None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'post with id: {id} is not found or not associtated with you.')
        
    return db_post


@router.post('/posts', response_model= PostResponse)
def create_post(post: PostCreate, db: Session= Depends(get_db), current_user:UserResponse= Depends(get_current_user) ):
    db_post= postService.get_post_by_title(db, post.title)
    if db_post:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= f'post with title: {post.title} already exists')

    return postService.create_post(db, post, current_user)


@router.delete('/posts/{id}', response_model= str)
def delete_post(id: int, db: Session= Depends(get_db), current_user:UserResponse= Depends(get_current_user) ):
    db_post= postService.get_post(db, id, current_user)
    if db_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'post with id: {id} is not found or not associtated with you.')
    
    return postService.delete_post(db, id)