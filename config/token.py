from datetime import datetime, timedelta
from jwt import PyJWTError
import jwt
from sqlalchemy.orm import Session
from database.connection import get_db
from services.user import UserService
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

from config.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception, db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        email: str = payload.get("sub")

        if email is None:
            raise credentials_exception
        token_data = email
    except PyJWTError:
        raise credentials_exception

    user = UserService.get_user(email=token_data, db=db)

    if not user:
        raise credentials_exception

    return user


def get_currentUser(db: Session = Depends(get_db), data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return verify_token(token=data, credentials_exception=credentials_exception, db=db)
