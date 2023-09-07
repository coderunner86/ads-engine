# helpers/openai_request.py
import requests
import json
def get_openai_response(query):

    url = "https://8sng98bnme.execute-api.us-east-1.amazonaws.com/stage/"

    data = {"query": query}

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        result = response.json()
        response_body = result.get('body', {})  # Obtener el campo 'body' como un diccionario
        response_text = response_body.get('response', '')  # Obtener el campo 'response' dentro de 'body'

        return(response_text)
    else:
        return "¡No eres tú, soy yo!"
    