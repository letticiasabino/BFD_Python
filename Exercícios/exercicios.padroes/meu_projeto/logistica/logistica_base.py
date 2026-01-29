from abc import ABC, abstractmethod

class Logistica(ABC):

  @abstractmethod
  def cria_transporte(self):
    pass

  def planejar_entrega(self):
    transporte = self.cria_transporte()
    transporte.entregar()
    