from .logistica_base import Logistica
from .navio import Navio

class LogisticaMaritima(Logistica):
    def cria_transporte(self):
        return Navio()
