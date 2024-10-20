from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.token import get_currentUser

from schemas.sale import SaleCreate, Sale
from services.sale import SaleService
#db
from database.connection import get_db

router = APIRouter(prefix="/sales", tags=["Ventas"])


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
