# helpers/fetch_audiences.py
import requests

def fetch_custom_audiences():
    response = requests.get("https://customendpoint-1336d936cf4f.herokuapp.com/customaudiences")
    data = response.json()
    custom_audiences = [entry.get('custom_audience', '') for entry in data]
    return custom_audiences
