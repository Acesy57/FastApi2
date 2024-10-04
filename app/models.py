from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from .database import Base
#from sqlalchemy.orm import relationship




class Library(Base):
    __tablename__ = "books"


    id=Column(Integer, primary_key=True, nullable=True)
    user_id=Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title=Column(String, nullable=True)
    author=Column(String, nullable=True)
    isbn=Column(String, nullable=True)
    publication_year=Column(Integer,  nullable=False)
    available=Column(Boolean,nullable=True)
    #user = relationship("User")
    

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=True)
    email = Column(String, nullable=True, unique=True)
    password = Column(String, nullable=True)