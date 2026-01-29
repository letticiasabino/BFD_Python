#1. Crie um programa que solicite ao usuário o preço de três produtos e calcule o valor total da compra.

p1 = float(input("Insira o valor do 1 produto:"))
p2 = float(input("Insira o valor do 2 produto:"))
p3 = float(input("Insira o valor do 3 produto:"))

calc = p1 + p2 + p3

print("O valor total da compra é:R$", calc)

#2. Desenvolva um programa que peça o ano de nascimento do usuário e o ano atual, e então calcule e exiba a idade do usuário.

nasc = int(input("Insira o ano do seu nascimento:"))
ano = int(input("Insira o ano atual:"))

calc = ano - nasc

print("A sua idade é:", calc)

#3. Escreva um programa que peça uma palavra ao usuário e um número inteiro, e então imprima a palavra repetida o número de vezes informado.

n = int(input("Insira um número inteiro:\n"))
palavra = input("Insira uma palavra:\n")

print("A palavra escolhida foi:",palavra)
print(palavra * n)

#4. Crie um programa que solicite o valor total de uma conta de restaurante e o número de pessoas para dividir a conta. Calcule e exiba o valor que cada pessoa deve pagar.

total = float(input("Insira o total da conta:\n"))
pessoas = int(input("Insira o total de pessoas a dividirem a conta:\n"))

calc = total / pessoas

print("O valor para cada integrante do grupo foi de:", calc)

#5. Desenvolva um programa que peça ao usuário para inserir as notas de três provas e calcule a média aritmética dessas notas.

p1 = float(input("Insira a nota 1:"))
p2 = float(input("Insira a nota 2:"))
p3 = float(input("Insira a nota 3:"))

calc = (p1 + p2 + p3) / 3

print("A sua média foi:", calc)


# 6. Escreva um programa que peça o peso (em kg) e a altura (em metros)  de uma pessoa e calcule o seu Índice de Massa Corporal (IMC), usando a fórmula: IMC = peso / (altura ** 2).

peso = float(input("Insira o seu peso(kgs):"))
altura = float(input("Insira a sua altura(metros):"))

IMC = peso / (altura ** 2)

print("O seu imc é dê:", IMC)

# 7. Crie um programa que receba um número total de segundos e o converta para horas, minutos e segundos, exibindo o resultado.

total = int(input("Insira um total de segundos:"))

minuto = total // 60
resto_segundos = total % 60
hora = minuto // 60
resto_minuto = minuto % 60

print(minuto)
print(resto_segundos)
print(hora)