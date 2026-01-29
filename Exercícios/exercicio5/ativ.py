# Produza uma classe livro, deve seer inicializada com o atributo autor.

class Livro:
    def __init__(self, autor): # Definindo um parametro para a classe livro
        self.autor = autor # Valor; Self serve para referenciar o objeto, o diferenciando dos demais. Ou seja, todos os objetos seguintes serão iguais.
        self.capitulo = []

# Método na classe livro que deve adicionar capítulos ao livro.
    def Adicionar_cap(self, capitulos):
        self.capitulo.append(capitulos)

# Produza uma classe capítulo, essa classe deve ser inicializada com um texto.

class Capitulo:
    def __init__(self, texto): # Parametro
        self.texto = texto # Valor

armadilhas = Livro(autor ="Augusto Cury")
capi = Capitulo(texto ="Uma fazenda bela e misteriosa")
armadilhas.Adicionar_cap(capi)

print(f'{armadilhas} foi adicionado com sucesso!')