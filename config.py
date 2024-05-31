# config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BIGQUERY_PROJECT_ID = 'tu_proyecto'
