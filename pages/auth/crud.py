from fastapi import HTTPException
from sqlalchemy.orm import Session
from . import model,scheme

class UserService:
    def __init__(self,db:Session):
        self.__db = db

    def get_user(self,  user_id:int):
        user = self.__db.query(model.User).filter(model.User.id == user_id).first()
        if user is None:
            user = HTTPException(status_code=404, detail='User not found')
        return user

    def get_user_by_email(self, user_email:str):
        user = self.__db.query(model.User).filter(model.User.email == user_email).first()
        if user is None:
            user = HTTPException(status_code=404, detail='User not found')
        return user

    def create_user(self, user:scheme.UserCreate):
        hashed_key = user.password
        hashed_salt = user.password
        new_user = model.User(name=user.name,email=user.email,key = hashed_key,salt=hashed_salt)
        self.__db.add(new_user)
        self.__db.commit()
        self.__db.refresh(new_user)
        return new_user