import requests
import json

# Autenticação usando OAuth 2.0
auth_response = requests.post(
    'https://api.contaazul.com/auth/oauth/token',
    headers={'Content-Type': 'application/x-www-form-urlencoded'},
    data={
        'client_id': 'seu_client_id',
        'client_secret': 'seu_client_secret',
        'grant_type': 'client_credentials'
    }
)
auth_response_json = json.loads(auth_response.text)
access_token = auth_response_json['access_token']

# Obtenção de informações de clientes
clientes_response = requests.get(
    'https://api.contaazul.com/v1/customers',
    headers={'Authorization': f'Bearer {access_token}'}
)
clientes_json = json.loads(clientes_response.text)
clientes = clientes_json['items']
