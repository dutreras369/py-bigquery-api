import os
from google.cloud import bigquery
from google.auth import credentials
from google.oauth2 import service_account
import pandas as pd
import logging
from config import CREDENTIALS_PATH, Config

class DataModel:
    def __init__(self):
        credentials_path = CREDENTIALS_PATH
        self.credentials = service_account.Credentials.from_service_account_file(credentials_path)
        self.client = bigquery.Client(credentials=self.credentials, project=Config.BIGQUERY_PROJECT_ID)
        self.table_id = f"{Config.BIGQUERY_PROJECT_ID}.test_dataset.models" 

    def insert_data(self, data):
        try:
            df = pd.DataFrame(data)        
            schema = []
            for col in df.columns:
                if df[col].dtype.name.upper() == 'OBJECT':
                    schema.append(bigquery.SchemaField(col, 'STRING', mode='NULLABLE'))
                elif df[col].dtype.name.upper() == 'INT64':
                    schema.append(bigquery.SchemaField(col, 'INTEGER', mode='NULLABLE'))
                elif df[col].dtype.name.upper() == 'FLOAT64':
                    schema.append(bigquery.SchemaField(col, 'FLOAT', mode='NULLABLE'))
                elif df[col].dtype.name.upper() == 'BOOL':
                    schema.append(bigquery.SchemaField(col, 'BOOLEAN', mode='NULLABLE'))
                elif df[col].dtype.name.upper() == 'DATETIME64[ns]':
                    schema.append(bigquery.SchemaField(col, 'TIMESTAMP', mode='NULLABLE'))
                else:
                    schema.append(bigquery.SchemaField(col, 'STRING', mode='NULLABLE'))

            schema.append(bigquery.SchemaField('comments', 'STRING', mode='REPEATED'))
            job_config = bigquery.LoadJobConfig(schema=schema)
            job = self.client.load_table_from_dataframe(df, self.table_id, job_config=job_config)
            job.result()
            return True 
        except Exception as e:
            logging.error(f"Error al insertar datos en BigQuery: {e}")
            return False

    def fetch_data_from_bigquery(self):
        query = f"SELECT * FROM `{self.table_id}`"
        df = self.client.query(query).to_dataframe()
        data = df.to_dict(orient='records')
        return data
