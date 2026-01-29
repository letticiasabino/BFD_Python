from abc import ABC, abstractmethod


class ProcessadorDeArquivo(ABC):
  
  @abstractmethod
  def lerArquivo(self, caminho):
    pass

  @abstractmethod
  def analisarConteudo(self, conteudo):
    pass

  def salvarNoBanco(self, registros):
    for r in registros:
      print(f"Salvando registos[{r}] no DB...")

  def processar(self, caminho):
    conteudo = self.lerArquivo(caminho)
    registros = self.analisarConteudo(conteudo)
    self.salvarNoBanco(registros)
    return f"Processados {len(registros)} registros."