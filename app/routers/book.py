from fastapi import  Depends, status, HTTPException, APIRouter, Request, Response
from .. import models, schema,oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from typing import Optional


router = APIRouter()

@router.get("/books")
def get_books(request: Request, db:Session = Depends(get_db), search:Optional[str] = (""),user_id: int = Depends(oauth2.get_current_user)):

    # print(request.query_params.items())
    # title = request.query_params.get("title")
    # author = request.query_params.get("author")

    books = db.query(models.Library).filter(models.Library.title.contains(search)).all()

    # print("This is the title", title)
    # print("This is author", author)

    # if title is not None:    
    #     book_query = book_query.filter(models.Library.title == title)
    
    # if author is not None:
    #     book_query = book_query.filter(models.Library.author == author)

    # book = book_query.all()

    return books

@router.get("/addbook")
def add_books(db:Session = Depends(get_db),user_id: int = Depends(oauth2.get_current_user)):
    books = db.query(models.Library).all
    return books

@router.post("/books", status_code=status.HTTP_201_CREATED, response_model=schema.BookResponse)
def create_book(book: schema.Library, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    new_book = models.Library(user_id=current_user.id, **book.dict())

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book

@router.get("/books/{id}")
def get_books(id: int, db:Session = Depends(get_db),user_id: int = Depends(oauth2.get_current_user)):  # noqa: F811
    books = db.query(models.Library).filter(models.Library.id==id).first()

    if not books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"book with id: {id} was not found")
    
    return books

@router.put("/books/{id}")
def update_book(id: int, book:schema.Library, db:Session = Depends(get_db),user_id: int = Depends(oauth2.get_current_user)):
        books_query = db.query(models.Library).filter(models.Library.id==id)
        books = books_query.first()
        if books is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"book with id:{id} does not exist ")
        books_query.update(book.dict(), synchronize_session=False)
        db.commit()
        return books_query.first()

@router.delete("/books/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_books(id:int,  db:Session = Depends(get_db),user_id: int = Depends(oauth2.get_current_user)):
    books = db.query(models.Library).filter(models.Library.id == id)
    if books.first() is None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"book with id:{id} does not exist ")
     
    books.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

