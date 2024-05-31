import os

# Obtener la ruta al directorio de las credenciales
CREDENTIALS_DIR = os.path.join(os.path.dirname(__file__), 'credentials')

# Ruta completa al archivo de credenciales
CREDENTIALS_PATH = os.path.join(CREDENTIALS_DIR, 'db-bigquery-425013-ab2c5a026bd8.json')

class Config:
    # Clave secreta para la aplicación Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta'

    # ID de proyecto de BigQuery
    BIGQUERY_PROJECT_ID = 'db-bigquery-425013'

    # Cargar credenciales desde el archivo JSON
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = CREDENTIALS_PATH
