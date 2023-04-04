import requests
import json

def import_purchase(access_token, purchase_data):
    url = "https://api.contaazul.com/v1/purchase"

    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(purchase_data))

    if response.status_code == 201:
        print("Compra importada com sucesso!")
    else:
        print("Erro ao importar a compra.")
        print("Código de status HTTP: ", response.status_code)
        print("Mensagem de erro: ", response.text)

def import_sale(access_token, sale_data):
    url = "https://api.contaazul.com/v1/sale"

    headers = {
        "Authorization": "Bearer " + access_token,
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers, data=json.dumps(sale_data))

    if response.status_code == 201:
        print("Venda importada com sucesso!")
    else:
        print("Erro ao importar a venda.")
        print("Código de status HTTP: ", response.status_code)
        print("Mensagem de erro: ", response.text)
