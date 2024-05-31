from flask import render_template, redirect, url_for, jsonify
from app.controllers import api_bp
import requests
import pandas as pd
from google.cloud import bigquery
from google.auth import default
from app.config import Config
import logging

credentials, project_id = default()
client = bigquery.Client(credentials=credentials, project=project_id)

@api_bp.route('/')
def index():
    return render_template('index.html')

@api_bp.route('/fetch_data', methods=['GET'])
def fetch_data():
    url = 'https://k51qryqov3.execute-api.ap-southeast-2.amazonaws.com/prod/makes/ckl2phsabijs71623vk0?modelsPage=1'
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()

        if 'models' in data:
            df = pd.DataFrame(data['models'])
            table_id = f"{Config.BIGQUERY_PROJECT_ID}.tu_dataset.tu_tabla"
            job_config = bigquery.LoadJobConfig(schema=df.dtypes.to_dict())
            job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
            job.result()
            logging.info("Datos cargados en BigQuery correctamente.")
            return redirect(url_for('api.success'))
        else:
            logging.error("No se encontró el atributo 'models' en la respuesta de la API.")
            return "No se encontró el atributo 'models' en la respuesta de la API.", 400
    except requests.RequestException as e:
        logging.error(f"Error al realizar la solicitud HTTP: {e}")
        return "Error al realizar la solicitud HTTP.", 500

@api_bp.route('/success')
def success():
    return render_template('success.html')
