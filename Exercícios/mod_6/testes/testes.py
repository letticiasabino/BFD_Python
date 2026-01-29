"""
Para que possamos contruir boas aplicações é fundamental que saibamos construir testes.
Eles não servem apenas para encontrar bugs e erros, eles ajudam a evitar que a aplicação regrida a medida que é desenvolvida. Pode parece contraditório,
mas a cada novos códigos adicionados, precisamos garantir que os anteriores funcionam perfeitamente, e produzir testes que rodem automaticamente
é o melhor cenário para isso.


Vamos iniciar com as estruturas que o python fornece para a construção de testes unitários.
"""


#Função que iremos testar

def soma(a,b):
    return a + b

#Podemos contruir testes manuais com a estrutura assert.

assert soma(2,3) == 5, "Deveria ser 5"

assert soma(-1,1) == 0, "Deveria ser 0"

print("Todos os testes foram um sucesso.")
print("--"*20)
""" 
O assert é um estrutura bem simples, ele testa para saber se o resultado é True, se for, o teste passa.
Caso um teste não passe, o assert irá levantar um AssertionError."""

#assert soma(3,3) == 5, "Deveria ser 6"

