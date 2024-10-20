from sqlalchemy import Column, Integer, String
from database.connection import Base

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    cedula = Column(String, unique=True, index=True)
    name = Column(String)
    address = Column(String)
    phone = Column(String)
    email = Column(String, unique=True)
