""" Nesse exercício eu criei uma classe chamada Carro que representa um carro com os seguintes atributos: modelo, marca, ano de lançamento, potência, câmbio e preço de lançamento.
Além disso, criei métodos para retornar o valor de cada um desses atributos. Depois, criei três objetos da classe Carro com diferentes valores para os atributos e testei os métodos para mostrar as informações de cada carro."""

class Carro: # Classe que representa um carro e vai armazenar as informações do carro
    def __init__(self, modelo, marca, ano_lancamento, potencia, cambio, preco_lancamento):
        # Defininfo os atributos que cada carro vai ter
        self.modelo = modelo
        self.marca = marca
        self.ano_lancamento = ano_lancamento
        self.potencia = potencia
        self.cambio = cambio
        self.preco_lancamento = preco_lancamento

        # Metodo que retorna o atributo de cada carro

    def get_modelo(self):
        return self.modelo
        
    def get_marca(self):
        return self.marca
        
    def get_ano_lancamento(self):
        return self.ano_lancamento
        
    def get_potencia(self):
        return self.potencia
        
    def get_cambio(self):
        return self.cambio
       
    def get_preco_lancamento(self):
        return self.preco_lancamento
        
        # Agora vou criar 3 objetos da classe Carro e testar os métodos

carro1 = Carro("Civic", "Honda", 2020, 2.0, "Automático", 120000)
carro2 = Carro("Gol", "Volkswagen", 2018, 1.6, "Manual", 55000)
carro3 = Carro("Corolla", "Toyota", 2022, 2.0, "Automático", 150000)

# Testando os métodos e mostrando as informações de cada carro

print("Carro 1:", carro1.get_modelo(), "Marca: ", carro1.get_marca(), "Lançamento: ", carro1.get_ano_lancamento(), "Potência: ", carro1.get_potencia(), "Câmbio: ", carro1.get_cambio(), "Valor no lançamento: ", "R$", carro1.get_preco_lancamento())

print("Carro 2:", carro2.get_modelo(), "Marca: ", carro2.get_marca(), "Lançamento: ", carro2.get_ano_lancamento(), "Potência: ", carro2.get_potencia(), "Câmbio: ", carro2.get_cambio(), "Valor no lançamento: ", "R$", carro2.get_preco_lancamento())

print("Carro 3:", carro3.get_modelo(), "Marca: ", carro3.get_marca(), "Lançamento: ", carro3.get_ano_lancamento(), "Potência: ", carro3.get_potencia(), "Câmbio: ", carro3.get_cambio(), "Valor no lançamento: ", "R$", carro3.get_preco_lancamento())