from .transporte import Transporte

class Navio(Transporte):
  def entregar(self):
    print("Entrega por Navio iniciada...")