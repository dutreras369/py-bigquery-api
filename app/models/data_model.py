import os
from google.cloud import bigquery
from google.auth import credentials
from google.oauth2 import service_account
import pandas as pd
from config import CREDENTIALS_PATH, Config

class DataModel:
    def __init__(self):
        credentials_path = CREDENTIALS_PATH
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path)
        self.client = bigquery.Client(credentials=self.credentials, project=Config.BIGQUERY_PROJECT_ID)
        self.table_id = f"{Config.BIGQUERY_PROJECT_ID}.test_dataset.models" 

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
