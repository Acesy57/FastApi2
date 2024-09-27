from fastapi import FastAPI, Depends, status, HTTPException, Response
from . import models,schema
from.database import engine,SessionLocal, get_db
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from pydantic import BaseModel


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class Library(BaseModel):
    title : str
    author : str
    isbn : str
    publication_year : int
    

    

def get_db():
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

@app.get("/books")
def get_books(db:Session = Depends(get_db)):
     
    books = db.query(models.Library).all()

    return books


@app.get("/addbooks")
def add_books(db:Session = Depends(get_db)):
    books = db.query(models.Library).all
    return books

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

@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: Library, db: Session = Depends(get_db)):
    new_book = models.Library(**book.dict())

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

@app.get("/books/{id}")
def get_books(id: int, db:Session = Depends(get_db)):
    books = db.query(models.Library).filter(models.Library.id==id).first()

    if not books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"book with id: {id} was not found")
    
    return books

@app.put("/books/{id}")
def update_book(id: int, book:schema.Library, db:Session = Depends(get_db)):
        books_query = db.query(models.Library).filter(models.Library.id==id)
        books = books_query.first()
        if books == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"book with id:{id} does not exist ")
        books_query.update(book.dict(), synchronize_session=False)
        db.commit()
        return books_query.first()

@app.delete("/books/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_books(id:int,  db:Session = Depends(get_db)):
    books = db.query(models.Library).filter(models.Library.id == id)
    if books.first() == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"book with id:{id} does not exist ")
     
    books.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)