from flask import render_template
from app.controllers import view_bp
from app.models import DataModel

@view_bp.route('/view_data', methods=['GET'])
def view_data():
    data_model = DataModel()
    data = data_model.fetch_data_from_bigquery()
    return render_template('data_view.html', data=data)
