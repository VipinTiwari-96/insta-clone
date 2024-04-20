from sqlalchemy.orm import Session;
# models
from ..models import Post;
# schemas
from ..schemas.post import PostCreate;
from ..schemas.user import UserResponse;

def get_posts(db: Session, current_user: UserResponse):
    return db.query(Post).filter(Post.owner_id== current_user.id)


def get_post(db: Session, id: int, current_user: UserResponse):
    return db.query(Post).filter(Post.owner_id==current_user.id).filter(Post.id== id).first()


def get_post_by_title(db: Session, title: str):
    return db.query(Post).filter(Post.title== title).first()



def create_post(db: Session, post: PostCreate, current_user: UserResponse):
    new_post= Post(title= post.title, content= post.content, is_published= post.is_published, owner_id= current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def delete_post(db: Session, id: int):
    post= db.get(Post, id)
    db.delete(post)
    db.commit()
    return 'success'