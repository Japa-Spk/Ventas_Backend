from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.client import ClientCreate, Client
from services.client import ClientService
#db
from database.connection import get_db

router = APIRouter(prefix="/clients", tags=["Clientes"])


@router.post("/", response_model=Client)
def create_new_client(client: ClientCreate, db: Session = Depends(get_db)):
    """
    Crea un cliente

    Este path client crea una cliente en el sistema.

    Parameters:
        cedula: str
        name: str
        address: str
        phone: str
        email: str

    Retorna un json con información básica del cliente grabado:

        error: bool
        mensaje: str
    """
    return ClientService().create_client(db, client)
