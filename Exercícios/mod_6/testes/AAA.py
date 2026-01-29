"""
Para essa etapa de testes é sempre bom seguir a estrutura conhecida como AAA

Arrange
Act
Assert

Nada mais é do que:
1 - Arrange: Preparar o cenário para o teste, criar variáveis, objetos, instâncias e o que mais for necessário).
2 - Act: Executar o método que está sendo testado
3 - Assert: Verificar se o(s) resultado(s) obtido(s) é o esperado.


Para demonstrar esse método de organização, vamos utilizar um código ligeiramente mais complexo,
ele nos permite perceber como assert continua funcionando de forma simples mesmo em estruturas mais robustas.
"""
from fibo import fibonacci

fibo_ord = { i : j for i,j in enumerate(fibonacci(10))} #guarda cada resultado do iterador numa posição do dicionário.

print("\n sequência enumerada no dicionário: \n")
print("=="*40)
print(fibo_ord)
print("=="*40)


""" Vamos então criar nosso teste."""

class Test_fibo:
    def setup(self):
      #Nesta etapa de arrange caso eu precissasse construir uma base para o teste do método ele ficaria aqui.
      #Atributos, chaves de API, dados e quaisquer outras coisas que pudessem ser necessárias para executar o teste. 
      #Pesquise na documentação do python por: "test fixture"
       pass
        
    def test_fibo(self):
        #Aqui iremos efetuar o teste de fato.

        #Resultado esperado para aquela função:

        resultado = [1,2,3,5,8,13,21,34,55]

        assert resultado == [i for i in fibonacci(9)] #Note que agora o resultado não está sendo iterado para um dicionário, e sim para uma lista!
        print("Sucesso!")

teste = Test_fibo()

teste.test_fibo()