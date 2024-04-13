from sqlalchemy.orm import Session;
# models
from ..models import Post;
# schemas
from ..schemas.post import PostCreate;

def get_posts(db: Session):
    return db.query(Post).all()


def get_post(db: Session, id: int):
    return db.query(Post).filter(Post.id== id).first()


def get_post_by_title(db: Session, title: str):
    return db.query(Post).filter(Post.title== title).first()



def create_post(db: Session, post: PostCreate):
    new_post= Post(title= post.title, content= post.content, is_published= post.is_published, owner_id= post.owner_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def delete_post(db: Session, id: int):
    post= db.get(Post, id)
    db.delete(post)
    db.commit()
    return 'success'