from flask import Blueprint, render_template, redirect, url_for, current_app
from app.models.data_model import DataModel
import requests

api_blueprint = Blueprint('api', __name__)

@api_blueprint.route('/fetch_data', methods=['GET'])
def fetch_data():
    url = 'https://k51qryqov3.execute-api.ap-southeast-2.amazonaws.com/prod/makes/ckl2phsabijs71623vk0?modelsPage=1'
    response = requests.get(url)
    data = response.json()

    if 'models' in data:
        model_data = data['models']
        model = DataModel()
        model.insert_data(model_data)
        return redirect(url_for('api.success'))
    else:
        return "No se encontró el atributo 'models' en la respuesta de la API."

@api_blueprint.route('/success', methods=['GET'])
def success():
    return render_template('success.html')
