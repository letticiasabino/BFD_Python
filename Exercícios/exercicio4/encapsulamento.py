class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self._saldo = saldo_inicial
        self.__senha = "8486vivo"
    
    def consultar_saldo(self):
        return f"Olá {self.titular}, seu saldo é R$ {self._saldo}"
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            return f"Deposito de R$ {valor} realizado com sucesso."
        else:
            return "Saldo insuficiente ou valor inválido!"
    
    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            return f"Saque de R$ {valor} realizado com sucesso!"
        else:
            return "Saldo insuficiente ou valor inválido!"
        
    def __metodo_secreto(self):
        return "Este é um metodo interno que só deve ser usado dentro da classe"
    
minha_conta = ContaBancaria("Lettícia", 5000)

print(minha_conta.titular)
print(minha_conta.consultar_saldo())
print(minha_conta.depositar(1000))
print(minha_conta.sacar(2100))
print(minha_conta._saldo)
print(minha_conta._ContaBancaria__senha)
print(minha_conta.__metodo_secreto())