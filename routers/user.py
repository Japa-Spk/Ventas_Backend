from fastapi import APIRouter, Depends

from typing import List
from sqlalchemy.orm import Session

from database.connection import get_db
from models.user import User
from schemas.user import UserCreate, User as Userschema
from services.user import UserService
from config.token import get_currentUser

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=List[Userschema])
def getAllUser(db: Session = Depends(get_db), current_user = Depends(get_currentUser)):
    return UserService.get_allUser(db=db)


@router.post("/")
def createUser(user: UserCreate, db: Session = Depends(get_db), current_user = Depends(get_currentUser)):
    return UserService.create_user(db, user)


@router.get("/me", response_model=Userschema)
def getMe(current_user: User = Depends(get_currentUser)):
    return current_user


@router.put("/{userid}")
def updateUser(userid: int, user: Userschema, db: Session = Depends(get_db), current_user = Depends(get_currentUser)):
    return UserService.update_user(db=db, userid=userid, user=user)


@router.delete("/{userid}")
def deleteUser(userid: int, db: Session = Depends(get_db), current_user = Depends(get_currentUser)):
    return UserService.deleteUser(db=db, userid=userid)