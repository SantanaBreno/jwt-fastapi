from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import func 
from app.db.base import Base

class UserModel(Base):
    __tablename__ = "users"
    id = Column('user_id', Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', String, nullable=False)
    email = Column('email', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
    created_at = Column('created_at', DateTime, nullable=False, default=func.now())
    last_access = Column('last_access', DateTime, nullable=True)
