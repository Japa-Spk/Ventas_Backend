from sqlalchemy import Column, Integer, Float, ForeignKey
from database.connection import Base

class SaleDetail(Base):
    __tablename__ = "sale_details"

    id = Column(Integer, primary_key=True, index=True)
    sale_header_id = Column(Integer, ForeignKey("sale_headers.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    sale_value = Column(Float)
    calculated_iva = Column(Float)
