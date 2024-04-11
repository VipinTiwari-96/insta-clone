from sqlalchemy.orm import Session;
# models
from ..models import User;
# schemas
from ..schemas.user import UserCreate;

def get_users(db: Session):
    return db.query(User).all()



def get_user(db: Session, id: int):
    return db.query(User).filter(User.id== id).first()



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