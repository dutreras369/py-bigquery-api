from flask import Blueprint, jsonify, render_template
from .services import get_data_from_api, process_data
from .models import DataModel

bp = Blueprint('app', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/process_data', methods=['GET'])
def process_data_route():
    data = get_data_from_api()
    dataframes = process_data(data)
    model = DataModel(dataframes)
    model.insert_into_bigquery()
    return jsonify({"message": "Data processed and inserted into BigQuery successfully"})
