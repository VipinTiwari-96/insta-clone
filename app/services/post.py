from sqlalchemy.orm import Session;
from sqlalchemy import func;
# models
from ..models import Post, Vote;
# schemas
from ..schemas.post import PostCreate;
from ..schemas.user import UserResponse;

def get_posts(db: Session):
    result= db.query(Post, func.count(Vote.post_id).label('vote_count')).outerjoin(Vote, Post.id==Vote.post_id).group_by(Post.id)
    posts_with_votes= []
    for post, vote_count in result:
        post_dict= post.__dict__
        post_dict['post_likes']= vote_count
        posts_with_votes.append(post_dict)

    return posts_with_votes


def get_post(db: Session, id: int):
    result= db.query(Post, func.count(Vote.post_id).label('vote_count')).outerjoin(Vote, Post.id== Vote.post_id).group_by(Post.id).filter(Post.id== id).first()

    # unpacking tuple
    post, vote_count= result 
    post_data= post.__dict__
    post_data['post_likes']= vote_count
    return post_data


def get_post_by_title(db: Session, title: str):
    return db.query(Post).filter(Post.title== title).first()



def create_post(db: Session, post: PostCreate, current_user: UserResponse):
    new_post= Post(title= post.title, content= post.content, is_published= post.is_published, owner_id= current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# deletion without retrieving the object into Python memory
def delete_post(db: Session, id: int, current_user:UserResponse):
    db.query(Post).filter(Post.id== id, Post.owner_id== current_user.id).delete()
    db.commit()
    return 'success'