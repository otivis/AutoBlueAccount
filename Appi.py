#!/usr/bin/env python3
import json
import pyAzul
import datetime

API_URL = 'https://api.contaazul.com'

# Abre o arquivo com o token de acesso
with open('./auth/token.json', 'r') as read:
    data_read = json.load(read)
    ACCESS_TOKEN = data_read['access_token']

# Cria um objeto de vendas da API do Conta Azul
azul_sales = pyAzul.Sales(API_URL, ACCESS_TOKEN)

# Função para criar um novo objeto de venda com informações dinâmicas
def create_new_sale(emission_date, customer_id, product_id, value, description, due_date, payment_value, payment_due_date, observations, customer_document, customer_name, customer_type, custom_fields):
    
    # cria a data de competência, que é hoje usando o dateti
    competence_date = datetime.date.today().strftime('%Y-%m-%d')

    # direita  e esquerda do gil
    nova_venda_body = {
        "emission": emission_date,
        "status": "COMMITTED",
        "customer_id": customer_id,
        "customer": {
            "id": customer_id,
            "name": customer_name,
        },
        "products": [
            {
                "quantity": 1,
                "product_id": product_id,
                "value": value,
                "description": description
            }
        ],
        "payment": {
            "type": "CASH",
            "method": "OTHER",
            "installments": [
                {
                    "number": 1,
                    "value": payment_value,
                    "due_date": payment_due_date
                }
            ]
        },
        "total": value,
        "seller": {
            "id": "fe662476-7460-46a4-9237-da286e71606a",
            "name": "Vendedor BTC"
        },
        "competence_date": competence_date,
        "due_date": due_date,
        "category": "Receita de Vendas",
        "observations": observations,
        "customer_document": customer_document,
        "customer_name": customer_name,
        "customer_type": customer_type,
        "custom_fields": custom_fields,
        "payment_provider": "Bitcoin",
        "payment_method": "Bitcoin",
        "payment_info": "1234567890abcdefg"
    }
    
    return nova_venda_body

# Cria um novo objeto de venda com informações dinâmicas
nova_venda_body = create_new_sale(
    emission_date="2023-05-02",
    customer_id="0e3b4ed1-604e-47da-b066-44f4b0f37754",
    product_id="f6190659-272b-4028-975f-7f4b4fdfe8ca",
    value=50000,
    description="idbinance",
    due_date="2023-06-02",
    payment_value=50000,
    payment_due_date="2023-06-02",
    observations="Observações sobre a venda de BTC",
    customer_document="000.000.000-00",
    customer_name="Cliente de BTC",
    customer_type="INDIVIDUAL",
    custom_fields={
        "Tipo de Criptomoeda": "BTC"
    }
)

# Envia a nova venda
response = azul_sales.new_sale(nova_venda_body)

# Verifica se


# Verifica se a resposta da API foi bem-sucedida
if 'id' in response:
    print("Venda criada com sucesso! ID da venda:", response['id'])
else:
    print("Erro ao criar a venda:", response)
