from sqlalchemy.orm import Session, joinedload;
# models
from ..models import User;
# schemas
from ..schemas.user import UserCreate;


def get_users(db: Session):
    return db.query(User).options(joinedload(User.posts)).all()



def get_user_by_id(db: Session, id: int):
    return db.query(User).options(joinedload(User.posts)).filter(User.id== id).first()


def get_user_by_username(db: Session, user_name: str):
    return db.query(User).filter(User.user_name== user_name).first()


def create_user(db: Session, user: UserCreate):
    new_user= User(user_name= user.user_name, age= user.age)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def delete_user(db: Session, id: int):
    user= db.get(User, id)
    db.delete(user)
    db.commit()
    return 'success'