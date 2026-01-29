from .logistica_base import Logistica
from .caminhao import Caminhao

class LogisticaTerrestre(Logistica):
    def cria_transporte(self):
        return Caminhao()
