from flask import render_template, redirect, url_for, jsonify
from app.controllers import api_bp
import requests
from app.models import DataModel
import logging

data_model = DataModel()

@api_bp.route('/fetch_data', methods=['GET'])
def fetch_data():
    url = 'https://k51qryqov3.execute-api.ap-southeast-2.amazonaws.com/prod/makes/ckl2phsabijs71623vk0?modelsPage=1'
    try:
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        
        models_data = data.get('models', {}).get('models', [])
        if not models_data:
            logging.error("No se encontraron modelos en la respuesta de la API.")
            return jsonify({"error": "No se encontraron modelos en la respuesta de la API."}), 400
        
        if data_model.insert_data(models_data):
            logging.info("Datos insertados en BigQuery correctamente.")
            return redirect(url_for('api.success'))
        else:
            logging.error("Error al insertar datos en BigQuery.")
            return jsonify({"error": "Error al insertar datos en BigQuery."}), 500
    except requests.RequestException as e:
        logging.error(f"Error al realizar la solicitud HTTP: {e}")
        return jsonify({"error": "Error al realizar la solicitud HTTP."}), 500

@api_bp.route('/success', methods=['GET'])
def success():
    return render_template('success.html')
