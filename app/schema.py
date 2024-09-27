from pydantic import BaseModel


class Library(BaseModel):
    title : str
    author : str
    isbn : str
    publication_year : int
    available : bool


    

class Config:
        orm_mode = True