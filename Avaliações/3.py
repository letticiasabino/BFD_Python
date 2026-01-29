""" Nesse exercício eu criei uma classe Planeta que representa um planeta com os seguintes atributos: nome, raio_equatorial, distância do sol e composição. """

class Planeta: # Classe que representa um planeta e vai armazenar as informações do planeta
    def __init__(self, nome, raio_equatorial, distancia_sol, composicao):
        # Defininfo os atributos que cada planeta vai ter
        self.nome = nome 
        self.raio_equatorial = raio_equatorial # Criem em KM
        self.distancia_sol = distancia_sol # Criem em milhões de KM
        self.composicao = composicao # Rochoso ou gasoso

        # Metodo para apresentar as informações do planeta

    def apresentacao(self):

        print(f"Planeta: {self.nome}\nRaio Equatorial: {self.raio_equatorial} km\nDistância do Sol: {self.distancia_sol} milhões de km\nComposição: {self.composicao}\n")


# Função fora da classe para calcular  a distância em UA (Unidade Astronômica)

def calcular_distancia_em_ua(distancia_sol): # Cada UA é aproximadamente 150 milhões de KM 

    return distancia_sol / 150 # Divido a distância em milhões de KM por 150
    return distancia_ua

# Agora vou pesquisar 3 planetas do sistema solar e criar objetos da classe Planeta
# Dados baseados em informações aproximadas:

terra = Planeta("Terra", 6371, 150, "Rochoso")
marte = Planeta("Marte", 3389, 228, "Rochoso")
jupiter = Planeta("Júpiter", 69911, 778, "Gasoso")

# Apresentação de cada planeta

terra.apresentacao()

marte.apresentacao()

jupiter.apresentacao()


# Calculando agora a distância em UA (Unidade Astronômica) para cada planeta

print(f"A Terra está a aproximadamente {calcular_distancia_em_ua(terra.distancia_sol):.2f} UA do Sol.")

print(f"O Marte está a aproximadamente {calcular_distancia_em_ua(marte.distancia_sol):.2f} UA do Sol.")

print(f"O Júpiter está a aproximadamente {calcular_distancia_em_ua(jupiter.distancia_sol):.2f} UA do Sol.")