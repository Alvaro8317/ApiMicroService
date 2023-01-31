import requests
baseURL = "http://127.0.0.1:8010/api/v1/customerdata/"


def create_data():
    data = requests.get(baseURL)
    return data.json()