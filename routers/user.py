from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database.connection import get_db
from models.user import User
from schemas.user import UserCreate
from services.user import UserService
from config.token import get_currentUser

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def getAllUser(db: Session = Depends(get_db)):
    return UserService.get_allUser(db=db)


@router.post("/")
def createUser(user: UserCreate, db: Session = Depends(get_db)):
    return UserService.create_user(db, user)


@router.get("/me")
def getMe(current_user: User = Depends(get_currentUser)):
    return current_user


@router.put("/{userid}")
def updateUser(userid: int, user: UserCreate, db: Session = Depends(get_db)):
    return UserService.update_user(db=db, userid=userid, user=user)


@router.delete("/{userid}")
def deleteUser(userid: int, db: Session = Depends(get_db)):
    return UserService.deleteUser(db=db, userid=userid)