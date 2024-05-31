import requests
import pandas as pd

def get_data_from_api():
    url = "https://k51qryqov3.execute-api.ap-southeast-2.amazonaws.com/prod/makes/ckl2phsabijs71623vk0?modelsPage=1"
    response = requests.get(url)
    data = response.json()
    return data

def process_data(data):
    models_data = data.get("models", [])
    dataframes = []
    for model in models_data:
        df = pd.DataFrame(model)
        dataframes.append(df)
    return dataframes
