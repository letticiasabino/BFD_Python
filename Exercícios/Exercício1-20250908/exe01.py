# Manipulando arquivo de nomes

# A - Ler o conteúdo do arquivo "nomes.txt" e exibir na tela
with open("nomes.txt", "r", encoding="utf-8") as arquivo:
    nomes = arquivo.readlines()
    print("Conteúdo original do arquivo:")
    print(nomes)

# B - Limpar e formatar os nomes
nomes_limpos = [nome.strip().title() for nome in nomes]
print("\nNomes formatados:")
for name in nomes_limpos:
    print(name)

# C - Salvar no arquivo "nomes_limpos.txt"
with open("nomes_limpos.txt", "w", encoding="utf-8") as arquivo_limpo:
    for nome in nomes_limpos:
        arquivo_limpo.write(nome + "\n")
print("\nNomes salvos em 'nomes_limpos.txt'.")

# Exercício 2 - Manipulando arquivo de vendas.csv

import csv

# A - Ler o conteúdo do arquivo "vendas.csv" e exibir na tela

with open("vendas.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    dados = list(leitor)

print("Conteúdo original do arquivo vendas.csv:")
for linha in dados:
    print(linha)

# B - Calcular o total de vendas
total_vendas = 0
for linha in dados[1:]:
    quantidade = int(linha[1])
    preco = float(linha[2])
    total_vendas += quantidade * preco

# C - Mostrar valor total
print(f"\nValor total de vendas: R$ {total_vendas:.2f}")

# Exercício 3 - Calculadora

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b

while True:
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        print("Saindo da calculadora... Até mais!")
        break

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == "1":
            print(f"Resultado: {soma(num1, num2)}")
        elif opcao == "2":
            print(f"Resultado: {subtracao(num1, num2)}")
        elif opcao == "3":
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif opcao == "4":
            print(f"Resultado: {divisao(num1, num2)}")
        else:
            print("Opção inválida, tente novamente.")

    except ValueError as erro:
        print(f"Erro: {erro}")

