from google.cloud import bigquery
from google.auth import default
from config import Config
import pandas as pd

class DataModel:
    def __init__(self):
        credentials, project_id = default()
        self.client = bigquery.Client(credentials=credentials, project=Config.BIGQUERY_PROJECT_ID)
        self.table_id = f"{Config.BIGQUERY_PROJECT_ID}.tu_dataset.tu_tabla"  # Reemplazar con tu dataset y tabla de BigQuery

    def insert_data(self, data):
        df = pd.DataFrame(data)
        schema = [bigquery.SchemaField(col, df[col].dtype.name.upper()) for col in df.columns]        
        job_config = bigquery.LoadJobConfig(schema=schema)
        job = self.client.load_table_from_dataframe(df, self.table_id, job_config=job_config)
        job.result()

    def fetch_data_from_bigquery(self):
        query = f"SELECT * FROM `{self.table_id}`"
        df = self.client.query(query).to_dataframe()
        data = df.to_dict(orient='records')
        return data
