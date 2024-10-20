from fastapi import FastAPI
from fastapi.responses import HTMLResponse

#db
from database.connection import engine, Base

# middlewares
from middlewares.error_handler import ErrorHandler
from fastapi.middleware.cors import CORSMiddleware

# routers
from routers import client
from routers import product
from routers import sale


app = FastAPI()
app.title = "Ventas-Api"
app.version = "0.1"

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Incluir rutas
app.include_router(client.router)
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
    