from abc import ABC, abstractmethod # Importando de dentro da função a biblioteca e o método decorator

class BaseGatewayPagamento(ABC):

    @abstractmethod
    def processar_pagamento(self, valor_total):
        pass


class GatewayPix(BaseGatewayPagamento):

    def processar_pagamento(self, valor_total):
        print(f"Processando R${valor_total:.2f} via PIX. Gerando QR Code...")

class GatewayCartaoCredito(BaseGatewayPagamento):

    def processar_pagamento(self, valor_total):
        print(f"Processando R${valor_total:.2f} via Cartão de Crédito. Conectando à  operadora...")

class GatewayCartaoDebito(BaseGatewayPagamento):

    def processar_pagamento(self, valor_total):
        print(f"Processando R${valor_total:.2f} via Cartão de Débito. Conectando à operadora...")