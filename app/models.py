from sqlalchemy import Column, Integer, String, Boolean 
from .database import Base






class Library(Base):
    __tablename__ = "books"


    id=Column(Integer, primary_key=True, nullable=True)
    title=Column(String, nullable=True)
    author=Column(String, nullable=True)
    isbn=Column(String, nullable=True)
    publication_year=Column(Integer,  nullable=False)
    available=Column(Boolean,nullable=True)