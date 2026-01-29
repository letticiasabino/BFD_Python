""" Nesse exercício eu criei uma classe (pai) chamada Cliente e uma classe (filha) chamada ContaCorrente que herda os atributos e métodos da classe Cliente. A classe ContaCorrente tem métodos para depositar, sacar e consultar o saldo da conta. Além disso, a classe Cliente tem um método para atualizar os dados do cliente. Depois, criei uma instância da classe ContaCorrente e testei os métodos para mostrar as informações do cliente e da conta."""

class Cliente: # Classe Cliente é o pai e a classe ContaCorrente vai ser a filha
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def mostrar_dados(self): # Esse método vai mostrar os dados do cliente
        return f"Nome: {self.nome}, CPF: {self.cpf}, Endereço: {self.endereco}"
    
    def atualizar_dados(self, nome=None, cpf=None, endereco=None):
        if nome:
            self.nome = nome
        
        if cpf:
            self.cpf = cpf
            
        if endereco:
            self.endereco = endereco
        
class ContaCorrente(Cliente): # Classe ContaCorrente é filha da classe Cliente
    def __init__(self, nome, cpf, endereco, numero_conta, saldo=0):
        super().__init__(nome, cpf, endereco) # Usando o super para herdar os atributos da classe pai
        self.__saldo = saldo # Atributo privado, não pode ser acesso diretamente fora da classe

    def depositar(self, valor): # Método para depositar dinheiro na conta
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor} realizado com sucesso. Saldo atual: R$ {self.__saldo}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor): # Método para sacar dinheiro da conta
        if valor > self.__saldo:
            print("Saldo insuficiente para saque.")

        elif valor <= 0:
            print("O valor do saque precisa ser positivo.")
        else:
            self.__saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso. Saldo atual: R$ {self.__saldo}")

    def consultar_saldo(self): # Método para consultar o saldo da conta
        return f"Saldo atual: R$ {self.__saldo}"
    
    def mostrar_informacoes(self): # Método para mostrar as informações do cliente e da conta
        return f"{self.mostrar_dados()}, {self.consultar_saldo()}"
    
# Criando uma instância da classe ContaCorrente e testando os métodos

conta1 = ContaCorrente("Lettícia Sabino", "123.456.789-00", "Rio de Janeiro - RJ", "51833-1", 2900)

# Testando deposito
conta1.depositar(100)

# Testando sacar mais do que tem na conta
conta1.sacar(3100)

# Sacando um valor inválido
conta1.sacar(-50)

# Consultando saldo
print(conta1.consultar_saldo())

# Mostrando as informações do cliente
print(conta1.mostrar_informacoes())

# Atualizando os dados do cliente
conta1.atualizar_dados(endereco="São Gonçalo - RJ")

print(conta1.mostrar_informacoes())
