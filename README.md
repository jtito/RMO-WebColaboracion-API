# RMO-WebColaboracion-API
Repositorio del proyecto Backend para el portal de colaboracion.
---
## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto localmente.

PARA TODA INSTALACION EL ENTORNO VIRTUAL DEBE ESTAR ENCENDIDO.

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




###Pasos para los tokens 
```bash

#Instalamos JWT para los tokens
pip install djangorestframework-simplejwt

#en settings.py

INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
    ...
]



## USANDO COVERAGE.PY
```bash

pip install pytest

#para trabajos con django
pip install pytest-django

#para verificar la version de pytest
pytest --version

#instalando coverage.py
pip install coverage

#ejecutar coverage.py
coverage run -m pytest

# Genera un informe en consola
coverage report

# Genera un informe HTML
coverage html
