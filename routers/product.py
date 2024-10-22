from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session

from config.token import get_currentUser

from schemas.product import ProductCreate, Product
from services.product import ProductService
#db
from database.connection import get_db

router = APIRouter(prefix="/products", tags=["Productos"])


@router.get("/", response_model=List[Product])
def getAllProduct(db: Session = Depends(get_db), current_user = Depends(get_currentUser)):
    return ProductService.get_allProduct(db=db)


@router.post("/", response_model=Product)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db), current_user = Depends(get_currentUser)):
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

@router.put("/{productid}")
def updateProduct(productid: int, product: ProductCreate, db: Session = Depends(get_db), current_user = Depends(get_currentUser)):
    return ProductService.update_product(db=db, productid=productid, product=product)


@router.delete("/{productid}")
def deleteProduct(productid: int, db: Session = Depends(get_db), current_user = Depends(get_currentUser)):
    return ProductService.deleteProduct(db=db, productid=productid)