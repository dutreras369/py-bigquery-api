from google.cloud import bigquery
from google.auth import default
from app.config import Config

class DataModel:
    def __init__(self):
        credentials, project_id = default()
        self.client = bigquery.Client(credentials=credentials, project=Config.BIGQUERY_PROJECT_ID)

    def insert_data(self, data):
        table_id = f"{Config.BIGQUERY_PROJECT_ID}.tu_dataset.tu_tabla"  # Reemplazar con tu dataset y tabla de BigQuery
        job_config = bigquery.LoadJobConfig(schema=[])  # Puedes agregar el esquema según tus necesidades
        job = self.client.load_table_from_json(data, table_id, job_config=job_config)
        job.result()
