import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta'
    BIGQUERY_PROJECT_ID = 'tu_proyecto'
