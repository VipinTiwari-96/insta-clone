from sqlalchemy.orm import Session;
# models
from ..models import Vote;
# schemas
from ..schemas.user import UserResponse;



def get_votes(db: Session, postId: int, current_user: UserResponse):
  return db.query(Vote).filter(Vote.post_id== postId, Vote.user_id== current_user.id).first()

def add_vote(db: Session, postId: int, current_user: UserResponse):
    vote= Vote(post_id= postId, user_id= current_user.id )
    db.add(vote)
    db.commit()
    return 'vote added.'


# deletion without retrieving the object into Python memory
def remove_vote(db: Session, postId: int, current_user: UserResponse):
    db.query(Vote).filter(Vote.post_id== postId, Vote.user_id== current_user.id).delete()
    db.commit()
    return 'vote remvoed.'