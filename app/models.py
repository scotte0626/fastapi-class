from sqlalchemy import Column,Integer,String,Boolean,Date
from .database import Base

class Todo(Base):
    __tablename__ = "todos"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(100),nullable=False)
    descripton = Column(String,nullable=True)
    completed= Column(Boolean,default=False)
    due_date=Column(Date,nullable=True)

class users(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(100),unique=True, nullable=False)
    password = Column(String(100),nullable=False)
    email = Column(String(100),unique=True, nullable=False)