# helpers/openai_request.py
import requests

def get_openai_response(best_match):
    payload = {
        "query": best_match
    }
    response = requests.post("https://8sng98bnme.execute-api.us-east-1.amazonaws.com/stage/", json=payload)
    if response.status_code == 200:
        data = response.json()
        ad_text = data['body']['response']
    return ad_text
