# VENTAS BACKEND

## Tecnologia
- **Python FastAPI**
- **Postgres SQL**
- **OAuth2**
- **JWT**
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

La `SECRET_KEY` que usas en tu archivo `.env` puede ser generada de manera aleatoria y debe ser única y difícil de adivinar. Aunque podrías inventarla manualmente, lo mejor es generar una clave segura para mejorar la seguridad de tu aplicación, especialmente si la estás utilizando para cosas como la firma de tokens JWT o la protección de sesiones.

### Cómo Generar una `SECRET_KEY` Segura

1. **Usando Python:**
   Puedes generar una clave secreta usando Python para asegurarte de que sea segura y aleatoria. Ejecuta el siguiente código en tu terminal o en un script de Python:

   ```python
   import secrets
   print(secrets.token_hex(32))
   ```

   Esto generará una clave hexadecimal de 64 caracteres (32 bytes), que es suficientemente segura para la mayoría de las aplicaciones.

2. **Usando Comandos en el Terminal:**
   En Linux o macOS, puedes usar el siguiente comando para generar una clave aleatoria:

   ```bash
   openssl rand -hex 32
   ```

   Esto también generará una cadena segura de 64 caracteres.

3. **Definir en el Archivo `.env`:**
   Una vez que tengas la clave generada, colócala en tu archivo `.env`:

   ```env
   SECRET_KEY=4e5d14d8f0c6b9a77d1b0e5a7d9158b2b5d8f027ab9ec6b248dd91b2f6e0a6c8
   ```

---
## **Datos por defecto**
Al momento de ejecutar el proyecto se crea un usuario por defecto con el rol de administrador, para poder crear productos y usuarios en el sistema.
- **User:** admin@admin.com
- **Password:** TEST.123