from fastapi import FastAPI
from . import models

from.database import engine,SessionLocal, get_db
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .routers import book, user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# class Library(BaseModel):
#     title : str
#     author : str
#     isbn : str
#     publication_year : int
    

    

def get_db():  # noqa: F811
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

my_books = [{"tiltle": "title of book 1", "author": "author of book 1" }, {"title": "mayour of iringa", "author": "a.abdra" }]

def find_book(title):
    for m in my_books:
        if m["title"] == title:
            return m

        
def find_index_book(title):
    for n, m in enumerate(my_books):
        if m['title'] == title:
            return n

@app.get("/")
def root():
    return {"message":'welcome to my api'}

app.include_router(book.router)
app.include_router(user.router)
app.include_router(auth.router)

while True:

    try:
        conn = psycopg2.connect(host='localhost', database='FastApi2', user='postgres',
        password='MECKLAUD', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successfully")
        break
    except Exception as error:
        print("connecting to database failed")
        print("error:", error)  
        time.sleep(1)  



