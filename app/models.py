from sqlalchemy import Column, Integer, String, DateTime, func;
# database
from .database import Base;


class User(Base):
    __tablename__= 'users'

    user_id= Column(Integer, primary_key=True, index=True, nullable=False)
    user_name= Column(String(50), unique=True, nullable=False)
    age= Column(Integer, nullable=False)
    created_at=  Column(DateTime(timezone=True), server_default= func.now(), nullable= False)
    updated_at= Column(DateTime(timezone=True), server_default= func.now(), nullable= False, onupdate=func.now())