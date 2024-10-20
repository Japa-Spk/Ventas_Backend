from pydantic import BaseModel, validator

class ProductBase(BaseModel):
    code: str
    name: str
    sale_value: float
    manages_iva: bool
    iva_percentage: float
    @validator('iva_percentage')
    def iva_mustn_be_greater_than_one(cls, v):
        if v > 1:
            raise ValueError('El iva tiene que ser menor a 1')
        return v
class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
