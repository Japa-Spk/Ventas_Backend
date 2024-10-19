from pydantic import BaseModel

class ProductBase(BaseModel):
    code: str
    name: str
    sale_value: float
    manages_iva: bool
    iva_percentage: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
