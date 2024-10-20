from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from config.token import create_access_token
from config.hashing import Hashing

from database.connection import get_db

from models.user import User


router = APIRouter(tags=["Authentication"])


@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    print("1")
    user = db.query(User).filter(User.email == request.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials"
        )
    print("2")
    if not Hashing.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password"
        )
    print("3")

    access_token = create_access_token(data={"sub": user.email})
    print("4")
    response = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "is_admin": user.is_admin,
        "is_active": user.is_active,
        "jwtToken": access_token,
    }

    return response