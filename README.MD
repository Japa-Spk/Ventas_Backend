# VENTAS BACKEND

## Instalación

### 1. Crear Entorno Virtual para Dependencias

Primero, asegúrate de tener Python instalado. Luego, crea un entorno virtual para gestionar las dependencias del proyecto:

```bash
python -m venv venv
```

Activa el entorno virtual:

- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```
- **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

### 2. Instalar Dependencias

Instala las dependencias necesarias desde el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Ejecutar FastAPI con Uvicorn

Para iniciar el servidor FastAPI, utiliza Uvicorn:

```bash
uvicorn main:app --reload --host 0.0.0.0
```

> **Nota**: El flag `--reload` permite la recarga automática durante el desarrollo. Cambia la dirección `--host` si es necesario para ajustarse a tu entorno.

## Configuración de Variables de Entorno

Crea un archivo `.env` en el directorio raíz del proyecto para configurar la base de datos y otras opciones de seguridad:

```env
# Configuración de la Base de Datos
DATABASE_URL=postgresql://postgres:TEST.123@192.168.0.23:5432/sales_db

# Modo de Depuración
DEBUG=True

# Configuración de Seguridad
SECRET_KEY="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=1440
```

### Descripción de Variables

- **`DATABASE_URL`**: La cadena de conexión para la base de datos PostgreSQL.
- **`DEBUG`**: Activa el modo de depuración (útil para desarrollo).
- **`SECRET_KEY`**: Clave secreta utilizada para firmar tokens JWT.
- **`ALGORITHM`**: Algoritmo utilizado para la codificación de tokens.
- **`ACCESS_TOKEN_EXPIRE_MINUTES`**: Tiempo de expiración de los tokens de acceso (en minutos).

> **Importante**: Asegúrate de mantener la `SECRET_KEY` segura y no exponerla en repositorios públicos.
