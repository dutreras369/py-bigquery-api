import logging
from flask import render_template
from app.controllers import view_bp
from app.models import DataModel

logger = logging.getLogger(__name__)

@view_bp.route('/view_data', methods=['GET'])
def view_data():
    try:
        data_model = DataModel()
        data = data_model.fetch_data_from_bigquery()
        return render_template('data_view.html', data=data)
    except Exception as e:
        logger.error(f"Error al obtener datos de BigQuery: {e}")
        return "Error al obtener datos de BigQuery", 500
