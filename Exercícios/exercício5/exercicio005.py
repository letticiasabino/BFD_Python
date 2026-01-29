# 1. Duas classes: Livro e Capítulo.

# Produza uma classe livro, deve seer inicializada com o atributo autor.
class Livro:
    def __init__(self, titulo, autor): # Definindo um parametro para a classe livro
        self.titulo = titulo
        self.autor = autor # Valor; Self serve para referenciar o objeto, o diferenciando dos demais. Ou seja, todos os objetos seguintes serão iguais.
        self.capitulo = [] # Atributo para receber a lista de capítulos.

# Método na classe livro que deve adicionar capítulos ao livro. (Instrução 5 e 6)
    def Adicionar_cap(self, capitulos):
        self.capitulo.append(capitulos)

# Método na classe livro para exibir os textos dos capítulos. (Instrução 7)
    def Exibir_textos(self):
        print(f"Livro: {self.titulo} \nAutor: {self.autor}")
        for i, cap in enumerate(self.capitulo, 1):
            # i é o índice, 1 para começar a contar do 1. cap.texto acessa o texto do objeto Capítulo.
            print(f"Capítulo {i}: {cap.texto}")
        print("--------------------")


# Produza uma classe capítulo, essa classe deve ser inicializada com um texto.
class Capitulo:
    def __init__(self, texto): # Parametro
        self.texto = texto # Valor

# Criando o livro 
armadilhas = Livro("Augusto Cury", "Armadilhas da mente")

# Criando o primeiro capítulo 
capi1 = Capitulo(texto ="Uma fazenda bela e misteriosa")
armadilhas.Adicionar_cap(capi1)

# Criando o segundo capítulo
capi2 = Capitulo(texto ="O mistério do velho celeiro.")

# Criando o terceiro capítulo

capi3 = Capitulo(texto ="Conclusão final e a liberdade.")

# Adicionando os novos capítulos ao livro
armadilhas.Adicionar_cap(capi2)
armadilhas.Adicionar_cap(capi3)

# Imprimindo o nome e autor do livro
print(f'O livro "{armadilhas.autor}" do autor "{armadilhas.titulo}" foi criado e recebeu os capítulos com sucesso!')

# Exibindo os textos contidos em cada capítulo
armadilhas.Exibir_textos()