from datetime import datetime
from typing import List
from pydantic import BaseModel, validator

#Cabecera
class SaleHeaderBase(BaseModel):
    date: datetime
    client_id: int
    total_sale: float
    @validator('total_sale')
    def total_sale_value_must_be_greater_than_zero(cls, v):
        if v <= 0:
            raise ValueError('El total de la venta tiene que ser mayor a 0')
        return v
        
class SaleHeaderCreate(SaleHeaderBase):
    pass

class SaleHeader(SaleHeaderBase):
    id: int
    consecutive: str

    class Config:
        orm_mode = True


#Detalle
class SaleDetailBase(BaseModel):
    product_id: int
    sale_value: float
    calculated_iva: float
    @validator('sale_value')
    def sale_value_must_be_greater_than_zero(cls, v):
        if v <= 0:
            raise ValueError('El valor del producto tiene que ser mayor a 0')
        return v

class SaleDetailCreate(SaleDetailBase):
    sale_header_id: int
    pass

class SaleDetail(SaleDetailBase):
    id: int

    class Config:
        orm_mode = True


#Cabecera Detalle
class SaleBase(BaseModel):
    header: SaleHeaderBase
    detail: List[SaleDetailBase]

class SaleCreate(SaleBase):
    pass

class Sale(SaleBase):
    pass