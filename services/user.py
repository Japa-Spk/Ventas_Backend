from sqlalchemy.orm import Session

from config.hashing import Hashing
from models.user import User
from schemas.user import UserCreate


class UserService:
    def get_allUser(db: Session):
        return db.query(User).all()

    def get_user(db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def get_user_id(db: Session, id: int):
        return db.query(User).filter(User.id == id).first()

    def create_user(db: Session, user: UserCreate):
        if UserService.get_user(db, user.email) is not None:
            raise Exception("El Usuario ya existe.")

        db_user = User(**user.dict())
        db_user.password = Hashing.bcrypt(db_user.password)

        db.add(db_user)
        
        try:
            db.commit()
            db.refresh(db_user)
            db_user.password = None
        except Exception as e:
            db.rollback()
            raise Exception("Error al crear el cliente. -> ") from e
        return db_user

    def update_user(db: Session, userid: int, user: UserCreate):
        db_userid = db.query(User).filter(User.id == userid).first()

        db_userid.name = user.name
        db_userid.email = user.email
        db_userid.password = Hashing.bcrypt(user.password)
        db_userid.is_admin = user.is_admin
        db_userid.is_active = user.is_active

        db.commit()

        return db_userid

    def deleteUser(db: Session, userid: int):
        db_userid = db.query(User).filter(User.id == userid).first()

        db.delete(db_userid)

        db.commit()

        return db_userid


    @staticmethod
    def create_default(db: Session):
        if not db.query(User).filter(User.email == "admin@admin.com").first():
            default_user = User(
                cedula="123456789",
                name="Admin",
                address="CLL 123",
                phone="5712345678",
                email="admin@admin.com",
                password=Hashing.bcrypt("TEST.123"),
                is_admin=True,
                is_active=True
            )
            db.add(default_user)
            db.commit()
            db.refresh(default_user)