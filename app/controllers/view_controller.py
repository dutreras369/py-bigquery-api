from flask import render_template
from app.controllers import view_bp
from google.cloud import bigquery
from google.auth import default
from app.config import Config

credentials, project_id = default()
client = bigquery.Client(credentials=credentials, project=project_id)

@view_bp.route('/view_data', methods=['GET'])
def view_data():
    table_id = f"{Config.BIGQUERY_PROJECT_ID}.tu_dataset.tu_tabla"
    df = client.query(f"SELECT * FROM `{table_id}`").to_dataframe()
    data = df.to_dict(orient='records')
    return render_template('data_view.html', data=data)
