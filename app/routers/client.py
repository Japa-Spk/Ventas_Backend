from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.client import ClientCreate, Client
from app.services.client import ClientService
#db
from app.database.connection import get_db

router = APIRouter()


@router.post("/clients/", response_model=Client, tags=['Clientes'])
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
