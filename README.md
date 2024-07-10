# RMO-WebColaboracion-API
Repositorio del proyecto Backend para el portal de colaboracion.
---
## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto localmente.


```bash
# Crea el entorno virtual
python -m venv venv

# Activa el entorno virtual (Windows)
venv\Scripts\activate

# Activa el entorno virtual (macOS/Linux)
source venv/bin/activate

# Instala Django
pip install django

# Instala Django REST Framework
pip install djangorestframework

#Para postgress
pip install psycopg2

#configurar en settings.py
#Los xxx configurar con su valores reales de su bd
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "xxxx",
        "USER": "xxxxx",
        "PASSWORD": "xxxxx",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
