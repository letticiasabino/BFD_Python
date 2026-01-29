from pagamentos import GatewayPix, GatewayCartaoCredito, GatewayCartaoDebito

def finalizar_compra(gateway, valor):
    gateway.processar_pagamento(valor)

gateway_pix = GatewayPix() # chamando o objeto pix

finalizar_compra(gateway_pix, 150.75)

gateway_cartao = GatewayCartaoCredito() # chamando o objeto crédito

finalizar_compra(gateway_cartao, 80.20)    

gateway_cartao1 = GatewayCartaoDebito() # chamando o objeto débito

finalizar_compra(gateway_cartao1, 1.00)

