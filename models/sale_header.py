from datetime import datetime

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database.connection import Base

class SaleHeader(Base):
    __tablename__ = "sale_headers"

    id = Column(Integer, primary_key=True, index=True)
    consecutive = Column(String, unique=True)
    date = Column(DateTime, default=datetime.utcnow)
    client_id = Column(Integer, ForeignKey("clients.id"))
    total_sale = Column(Float)

    client = relationship("Client")