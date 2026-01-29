from .base import ProcessadorDeArquivo

class ProcessadorTXT(ProcessadorDeArquivo):
    def lerArquivo(self, caminho):
        print(f"Lendo TXT: {caminho}")
        return "linha1\nlinha2\nlinha3"

    def analisarConteudo(self, conteudo):
        print("Analisando TXT...")
        return conteudo.split("\n")
