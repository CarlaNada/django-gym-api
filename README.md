# Gym Management API REST

API RESTful desarrollada para la gestión modular de un gimnasio.

## 🛠️ Tecnologías utilizadas
* Python 3.12+
* Django & Django REST Framework
* SQLite
* Manager de entornos: `uv`

## Cómo ejecutar el proyecto

1. Clonar el repositorio:
   ```
   git clone <URL_DEL_REPO>
   cd <NOMBRE_CARPETA>
   ```

2. Instalar dependencias e iniciar el entorno con uv:
    ```
    uv sync
    ```

3. Aplicar migraciones y levantar el servidor:
    ```
    cd src
    uv run python manage.py migrate
    uv run python manage.py runserver
    ```