from fastapi import APIRouter, Depends;
from sqlalchemy.orm import Session;
# schemas
from ..schemas.user import UserResponse, UserCreate;
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
    return userService.get_user(db, id)


@router.post('/users', response_model=UserResponse)
def create_user(user: UserCreate, db:Session= Depends(get_db)):
    return userService.create_user(db, user)


@router.delete('/users/{id}', response_model= str)
def delete_user(id: int, db:Session= Depends(get_db)):
    return userService.delete_user(db, id)
