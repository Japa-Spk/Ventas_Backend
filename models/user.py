from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database.connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    address = Column(String)
    phone = Column(String)
    password = Column(String)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)


    # def __repr__(self):
    #     return f"<User {self.email}"