from google.cloud import bigquery
from google.auth import default
from app.config import Config

class DataModel:
    def __init__(self):
        credentials, project_id = default()
        self.client = bigquery.Client(credentials=credentials, project=Config.BIGQUERY_PROJECT_ID)

    def insert_data(self, data):
        table_id = f"{Config.BIGQUERY_PROJECT_ID}.tu_dataset.tu_tabla"  # Reemplazar con tu dataset y tabla de BigQuery
        
        # Crear el esquema automáticamente a partir de los datos
        schema = []
        for key, value in data.items():
            if isinstance(value, int):
                schema.append(bigquery.SchemaField(key, "INTEGER"))
            elif isinstance(value, float):
                schema.append(bigquery.SchemaField(key, "FLOAT"))
            elif isinstance(value, str):
                schema.append(bigquery.SchemaField(key, "STRING"))
            elif isinstance(value, list):
                # Supongamos que los elementos de la lista son strings
                schema.append(bigquery.SchemaField(key, "STRING", mode="REPEATED"))
        
        job_config = bigquery.LoadJobConfig(schema=schema)
        job = self.client.load_table_from_json(data, table_id, job_config=job_config)
        job.result()

    def fetch_data_from_bigquery(self):
        query = f"SELECT * FROM `{table_id}`"
        df = self.client.query(query).to_dataframe()
        data = df.to_dict(orient='records')
        return data
