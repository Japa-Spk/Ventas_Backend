from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from config.token import get_currentUser

from models.user import User
from schemas.sale import SaleCreate, Sale, SaleHeaderResponse
from services.sale import SaleService
#db
from database.connection import get_db

router = APIRouter(prefix="/sales", tags=["Ventas"])


@router.get("/", response_model=List[SaleHeaderResponse])
def getAllUser(db: Session = Depends(get_db), current_user = Depends(get_currentUser)):
    return SaleService.get_all_sales(db=db)

@router.get("/me", response_model=List[SaleHeaderResponse])
def getMe(db: Session = Depends(get_db), current_user: User = Depends(get_currentUser)):
    print("current_user", current_user.id)
    return SaleService().get_all_sales_user(db, current_user.id)

@router.post("/", response_model=Sale)
def create_new_product(sale: SaleCreate, db: Session = Depends(get_db), current_user = Depends(get_currentUser)):
    """
    Crea un registro de venta

    Este path sales crea una registro de ventas en el sistema.

    Parameters:
        header: SaleHeaderBase
        detail: List[SaleDetailBase]

    Retorna un json con información básica del registro de ventas grabado:

        error: bool
        mensaje: str
    """
    return SaleService().create_sale(db, sale)
