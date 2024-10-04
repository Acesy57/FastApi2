from pydantic import BaseModel,EmailStr
from typing import Optional

class Library(BaseModel):
    title : str
    author : str
    isbn : str
    publication_year : Optional[int]
    available : bool

class UserOut(BaseModel):
      id:int
      email:EmailStr
      user_id:int
      class Config:
        orm_mode = True 
    

class BookResponse(Library):
     title : str
     author : str
     isbn : str
     user_id:int
     
     class congig:
         orm_mode = True


class UserCreate(BaseModel):
      email:EmailStr
      password:str

      class config:
            orm_mode = True



class UserLogin(BaseModel):
     email:EmailStr
     password:str

    #  class config:
    #       orm_mode = True

class Token(BaseModel):
     access_token:str
     token_type:str

     #class config:
      #    orm_mode = True

class TokenData(BaseModel):
     id: Optional[str] = None