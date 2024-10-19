from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.product import ProductCreate, Product
from app.services.product import ProductService
#db
from app.database.connection import get_db

router = APIRouter()


@router.post("/products/", response_model=Product, tags=['Productos'])
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Crea un producto

    Este path client crea una producto en el sistema.

    Parameters:
        code: str
        name: str
        sale_value: float
        manages_iva: bool
        iva_percentage: float

    Retorna un json con información básica del producto grabado:

        error: bool
        mensaje: str
    """
    return ProductService().create_product(db, product)
