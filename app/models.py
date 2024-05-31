from google.cloud import bigquery
from google.auth import default

# Obtén las credenciales de autenticación para BigQuery
credentials, project_id = default()

# Configura el cliente de BigQuery
client = bigquery.Client(credentials=credentials, project=project_id)

class DataModel:
    def __init__(self, dataframes, table_id):
        self.dataframes = dataframes
        self.table_id = table_id

    def insert_into_bigquery(self):
        for df in self.dataframes:
            table_id = "your_project.your_dataset.your_table"  # Reemplaza con tu proyecto, dataset y tabla de BigQuery
            job_config = bigquery.LoadJobConfig(schema=df.dtypes.to_dict())
            job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
            job.result()
