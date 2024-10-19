from sqlalchemy import Column, Integer, String, Boolean, Float
from app.database.connection import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    name = Column(String)
    sale_value = Column(Float)
    manages_iva = Column(Boolean, default=False)
    iva_percentage = Column(Float, nullable=True)
