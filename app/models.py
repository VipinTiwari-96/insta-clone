from sqlalchemy import Column, Integer, String, DateTime,Boolean, Text, func, ForeignKey;
from sqlalchemy.orm import relationship;
# database
from .database import Base;


class User(Base):
    __tablename__= 'users'

    id= Column(Integer, primary_key=True, index=True, nullable=False)
    user_name= Column(String(50), unique=True, nullable=False)
    password= Column(String(200))
    age= Column(Integer, nullable=False)
    created_at=  Column(DateTime(timezone=True), server_default= func.now(), nullable= False)
    updated_at= Column(DateTime(timezone=True), server_default= func.now(), nullable= False, onupdate=func.now())

    # relationship
    posts= relationship('Post', back_populates='owner', cascade='all, delete')



class Post(Base):
    __tablename__= 'posts'

    id= Column(Integer, primary_key=True, index=True, nullable=False)
    title= Column(String(50), nullable=False)
    content= Column(Text, nullable=True)
    is_published= Column(Boolean, default=False, nullable= False)
    owner_id= Column(Integer, ForeignKey('users.id'), nullable=False,)
    created_at=  Column(DateTime(timezone=True), server_default= func.now(), nullable= False)
    updated_at= Column(DateTime(timezone=True), server_default= func.now(), nullable= False, onupdate=func.now())

    # relationship
    owner= relationship('User', back_populates='posts',)
