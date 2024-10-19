from sqlalchemy.orm import Session
from app.models.client import Client
from app.schemas.client import ClientCreate

class ClientService:
    
    @staticmethod
    def create_client(db: Session, client: ClientCreate):
        if ClientService.client_exists(db, client.cedula):
            raise Exception("El cliente ya existe.")

        db_client = Client(**client.dict())
        db.add(db_client)
        try:
            db.commit()
            db.refresh(db_client)
        except Exception as e:
            db.rollback()
            raise Exception("Error al crear el cliente. -> ") from e
        return db_client

    @staticmethod
    def client_exists(db: Session, cedula: str) -> bool:
        return db.query(Client).filter(Client.cedula == cedula).first() is not None