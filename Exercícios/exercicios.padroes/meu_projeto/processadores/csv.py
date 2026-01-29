from .base import ProcessadorDeArquivo

class ProcessadorCSV(ProcessadorDeArquivo):
    def lerArquivo(self, caminho):
        print(f"Lendo CSV: {caminho}")
        return "nome,idade,cidade"

    def analisarConteudo(self, conteudo):
        print("Analisando CSV...")
        return conteudo.split(",")
