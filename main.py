from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
#db
from database.connection import engine, Base, SessionLocal

# middlewares
from middlewares.error_handler import ErrorHandler
from fastapi.middleware.cors import CORSMiddleware

# services
from services.user import UserService
# routers
from routers import auth
from routers import user
from routers import product
from routers import sale


app = FastAPI()
app.title = "Ventas-Api"
app.version = "0.1"

# Crear las tablas
@app.on_event("startup")
def on_startup():
    # Crea todas las tablas en la base de datos
    Base.metadata.create_all(bind=engine)
    # Crea sesión de la base de datos
    db:Session = SessionLocal()
    # Crea usuario por defecto
    UserService.create_default(db)
    # Cierra la sesión
    db.close()

# Incluir rutas
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(product.router)
app.include_router(sale.router)

app.add_middleware(ErrorHandler)

# Configuración de los encabezados CORS para pruebas correo
origins = [
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/', tags=['home'])
def message():
    return HTMLResponse(f'<h1>Api Ventas</h1>')

# despliegue en contenedor
# if __name__ == "__main__":
    # uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info") #windows
    # gunicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info") unix
    