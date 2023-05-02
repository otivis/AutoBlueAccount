# AutoBlueAccount
Tentando automotizar um processo no conta azul
usando a biblioteca do Robson Melo pyContaAzul
</h1>




****"emission": data de emissão da venda. Deve ser no formato "AAAA-MM-DD".

"status": estado atual da venda. Pode ser "COMMITTED" (confirmada) ou "DRAFT" (rascunho).

***"customer_id": ID do cliente relacionado à venda.

***"customer": objeto contendo informações do cliente relacionado à venda. Inclui "id" (ID do cliente) e "name" (nome do cliente).

***"products": array contendo objetos com informações dos produtos relacionados à venda. Cada objeto inclui "quantity" (quantidade), "product_id" (ID do produto), "value" (valor unitário) e "description" (descrição do produto).

**"payment": objeto contendo informações de pagamento da venda. Inclui "type" (tipo de pagamento), "method" (método de pagamento), e "installments" (parcelas).

***"total": valor total da venda.

***"seller": objeto contendo informações do vendedor relacionado à venda. Inclui "id" (ID do vendedor) e "name" (nome do vendedor).

"competence_date": data de competência da venda. Deve ser no formato "AAAA-MM-DD".

**"due_date": data de vencimento da venda. Deve ser no formato "AAAA-MM-DD".

***category": categoria da venda. PAdrão ou perosnalizada

***"observations": observações adicionais sobre a venda.

"custom_fields": campos personalizados adicionais.

"payment_provider": provedor de pagamento da venda.

***"payment_method": método de pagamento da venda.

"payment_info": informações adicionais de pagamento da venda
