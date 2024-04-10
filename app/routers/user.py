from fastapi import APIRouter;

from ..schemas.user import UserResponse;

router= APIRouter(
    tags=['Users']
)


@router.get('/users', response_model= list[UserResponse])
def get_users():
    return []

@router.get('/users/{user_id}', response_model= UserResponse)
def get_user(user_id: int):
    return {"id": 1, "user_name": "vipin", "age": 26, "created_at":'23/03/23', "updated_at":'28/09/23'}


@router.post('/users', response_model=UserResponse)
def create_user():
    return {}

@router.delete('/users/{user_id}', response_model= str)
def delete_user(user_id: int):
    return 'success'