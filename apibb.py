import zeep

# Autenticação usando certificado digital
cert = ('/path/to/cert.pem', '/path/to/key.pem')
client = zeep.Client(
    'https://cobranca.bb.com.br:7101/Processos/Ws/RegistroCobrancaService?wsdl',
    transport=zeep.transports.TlsTransport(
        ssl_context=zeep.transports.create_tls_client_context(),
        client_cert=cert,
    )
)

# Obtenção de informações de transações
transacoes = client.service.buscarTransacoes(
    dataInicio='2022-01-01',
    dataFim='2022-01-31',
    identificacao='12345678',
)
