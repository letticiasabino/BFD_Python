class Carro:
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.acoes = []  # lista vazia de ações

    def adicionar_acao(self, acao):
        self.acoes.append(acao)

    def exibir_acoes(self):
        print(f"\nAções realizadas pelo {self.marca} {self.modelo} ({self.ano}):")
        for acao in self.acoes:
            print(f"- {acao}")


# Criando o carro com informações do usuário
modelo = input("Digite o modelo do carro: ")
marca = input("Digite a marca do carro: ")
ano = int(input("Digite o ano do carro: "))

# Instanciando o objeto carro
meu_carro = Carro(modelo, marca, ano)

# Adicionando ações
meu_carro.adicionar_acao("Ligar")
meu_carro.adicionar_acao("Ajustar os assentos")
meu_carro.adicionar_acao("Passar a primeira marcha")
meu_carro.adicionar_acao("Acelerar")
meu_carro.adicionar_acao("Vruuuuum!")
meu_carro.adicionar_acao("Ops... Bateu! 💥")

# Exibindo todas as ações
meu_carro.exibir_acoes()