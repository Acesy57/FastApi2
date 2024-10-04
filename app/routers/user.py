from fastapi import  Depends, status, HTTPException, APIRouter
from .. import models, schema, utils
from sqlalchemy.orm import Session
from .. database import get_db

router = APIRouter()




@router.post("/users", status_code=status.HTTP_201_CREATED, response_model=schema.UserOut)
def create_user(user: schema.UserCreate, db: Session = Depends(get_db)):

    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/users/{id}", response_model=schema.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="user with id:{id} does not exist")
    return user