from fastapi import APIRouter, Depends, HTTPException, status;
from fastapi.security.oauth2 import OAuth2PasswordRequestForm;
from sqlalchemy.orm import Session;
# schemas
from ..schemas.user import UserCreate;
from ..schemas.auth import  AuthBase;
# services
from ..services import user as userService;
# db
from ..get_db import get_db;
from ..hashed_password import create_hash, verify_password;
from ..oauth2 import create_access_token;



router= APIRouter(
    tags=['Auth']
)


@router.post('/auth/create')
def create_user(user: UserCreate, db:Session= Depends(get_db)):
    db_user= userService.get_user_by_username(db, user.user_name)
    if db_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail= f'user with username: {user.user_name} already exists')
    
    user.password= create_hash(user.password)
    return userService.create_user(db, user)



@router.post('/auth/me', response_model=AuthBase)
def login(user: OAuth2PasswordRequestForm= Depends(), db:Session= Depends(get_db)):
    db_user= userService.get_user_by_username(db, user.username)
    if db_user is None :
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"credentials don't match." )
    
    if not verify_password(user.password, db_user.password):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"credentials don't match." )
    
    access_token= create_access_token(data={'user_id': db_user.id})
    return {'access_token': access_token, **db_user.__dict__}


