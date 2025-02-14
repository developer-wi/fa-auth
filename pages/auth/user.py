from fastapi import APIRouter,Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, Base, engine
from pages.auth.crud import UserService
from pages.auth.scheme import UserCreate


def get_db():
    #Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(
    prefix="/api/user"
)

@router.post("/create",tags=['user'])
def create_user(user:UserCreate, db:Session = Depends(get_db)):
    user_service = UserService(db)
    return user_service.create_user(user)

@router.get("/",tags=['user'])
def get_user(user_id:int,db:Session = Depends(get_db)):
    user_service=UserService(db)
    user = user_service.get_user(user_id)
    if str(type(user)) == "<class 'fastapi.exceptions.HTTPException'>":
        raise user
    return user

@router.get("/email",tags=['user'])
def get_user(user_email:str,db:Session = Depends(get_db)):
    user_service=UserService(db)
    user = user_service.get_user_by_email(user_email)
    if str(type(user)) == "<class 'fastapi.exceptions.HTTPException'>":
        raise user
    return user
