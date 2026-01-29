from .transporte import Transporte

class Caminhao(Transporte):
  def entregar(self):
    print("Entrega por Caminhão iniciada...")