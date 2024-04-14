from fastapi import APIRouter, Depends, HTTPException, status;
from sqlalchemy.orm import Session;
# schemas
from ..schemas.user import UserResponse;
# services
from ..services import user as userService;
# db
from ..get_db import get_db;

router= APIRouter(
    tags=['Users']
)


@router.get('/users', response_model= list[UserResponse])
def get_users(db:Session= Depends(get_db)):
    return userService.get_users(db)

@router.get('/users/{id}', response_model= UserResponse)
def get_user(id: int, db:Session= Depends(get_db)):
    db_user= userService.get_user_by_id(db, id)
    if db_user is None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'user with id: {id} is not found.')
    
    return db_user



@router.delete('/users/{id}', response_model= str)
def delete_user(id: int, db:Session= Depends(get_db)):
    db_user= userService.get_user_by_id(db, id)
    if db_user is None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f'user with id: {id} is not found.')
    
    return userService.delete_user(db, id)
