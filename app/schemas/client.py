from pydantic import BaseModel, validator

class ClientBase(BaseModel):
    cedula: str
    name: str
    address: str
    phone: str
    email: str

    @validator('cedula')
    def cedula_must_be_numeric(cls, v):
        if not v.isdigit():
            raise ValueError('La cédula debe ser numérica')
        return v

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int

    class Config:
        orm_mode = True
