import os
from dotenv import load_dotenv

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Acceder a las variables de entorno
DATABASE_URL = os.getenv("DATABASE_URL")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"