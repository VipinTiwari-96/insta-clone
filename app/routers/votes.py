from fastapi import APIRouter, Depends, HTTPException, status;
from sqlalchemy.orm import Session;
# schemas
from ..schemas.user import UserResponse;
# services
from ..services import vote as voteService;
from ..services import post as postService;
# db
from ..get_db import get_db;
from ..oauth2 import get_current_user;



router= APIRouter(
    tags=['votes']
)


@router.post('/posts/{id}/votes', response_model= str)
def vote(id:int, db:Session= Depends(get_db), current_user:UserResponse= Depends(get_current_user)):
    db_post= postService.get_post(db, id)
    if db_post is None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'post with id: {id} is not found.')
    
    user_post_vote= voteService.get_votes(db, id, current_user)
    if user_post_vote:
        return  voteService.remove_vote(db, id, current_user)
    return voteService.add_vote(db, id, current_user)