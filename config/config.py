import os

from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Acceder a las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
#Security data
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))