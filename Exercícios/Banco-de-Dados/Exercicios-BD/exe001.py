# Aula 14.10.2025


# Crie uma tabela e estabeleça conexão entre elas com as seguintes colunas: ID, nome, idade, cpf, email, endereço, sexo, salario.

import sqlite3
from turtle import update # Primeiro passo é importar o sqlite3

con = sqlite3.connect("cadastro.db") # Aqui estou criando o banco de dados

cursor = con.cursor() # Conectando o banco de dados com a tabela

print("Banco de dados conectado com sucesso!")


# Criando a tabela

cursor.execute("""CREATE TABLE IF NOT EXISTS CadastroCliente (  
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade NUMBER NOT NULL,
               cpf TEXT NOT NULL,
               email TEXT NOT NULL,
               endereço TEXT NOT NULL,
               sexo TEXT NOT NULL,
               salario NUMBER NOT NULL); """)

print("Tabela criada com sucesso!")

# Inserindo as informações 

cursor.execute("INSERT INTO CadastroCliente (nome, idade, cpf, email, endereço, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Lettícia Sabino", 26, "000.000.000-00", "letticiasabino@email.com", "São Gonaçalo", "F", "25000"))

cursor.execute("INSERT INTO CadastroCliente (nome, idade, cpf, email, endereço, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Thamara Araujo", 70, "100.100.100-10", "thamaraaraujo@email.com", "Rio de Janeiro", "F", "3500"))

cursor.execute("INSERT INTO CadastroCliente (nome, idade, cpf, email, endereço, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Luis Fernando", 26, "200.200.200-20", "luisfernando@email.com", "Brasília", "M", "2950"))

cursor.execute("INSERT INTO CadastroCliente (nome, idade, cpf, email, endereço, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Raissa Luiza", 25, "333.555.666-30", "raissaluiza@email.com", "Niterói", "F", "15000"))

cursor.execute("INSERT INTO CadastroCliente (nome, idade, cpf, email, endereço, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Murilo Bento", 36, "444.111.333-50", "murilobento@email.com", "Rio de Janeiro", "M", "2875"))

cursor.execute("INSERT INTO CadastroCliente (nome, idade, cpf, email, endereço, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Gabriel Salvador", 44, "555.777.888-30", "gabrielsalvador@email.com", "Niterói", "M", "10500"))

cursor.execute("INSERT INTO CadastroCliente (nome, idade, cpf, email, endereço, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Gabriel Felipe", 78, "111.999.555-70", "gabrielfelipe@email.com", "São Gonçalo", "M", "6200"))

cursor.execute("INSERT INTO CadastroCliente (nome, idade, cpf, email, endereço, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Lara Maria", 59, "111.999.200-20", "laramaria@email.com", "São Gonçalo", "F", "1509"))

cursor.execute("INSERT INTO CadastroCliente (nome, idade, cpf, email, endereço, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Maria Clara", 18, "353.578.999-20", "mariaclara@email.com", "São Paulo", "F", "3520"))

cursor.execute("INSERT INTO CadastroCliente (nome, idade, cpf, email, endereço, sexo, salario) VALUES (?, ?, ?, ?, ?, ?, ?)",
               ("Luis Felipe", 65, "147.517.522-92", "luisfelipe@email.com", "Minas Gerais", "M", "8520"))

print("Clientes cadastrados com sucesso.")

# Consultando os dados da tabela

cursor.execute("SELECT * FROM CadastroCliente;") # Selecionando todo o conteúdo da tabela CadastroCliente

resultado = cursor.fetchall() # Criando variável para guardar o resultado da consulta

print("Lista de Clientes\n")
print("=="*30)

for i in resultado:
    print(f"ID: {i[0]}, Cliente: {i[1]}, Idade: {i[2]}, CPF: {i[3]}, E-mail: {i[4]}, Endereço: {i[5]}, Sexo: {i[6]}, Salário: {i[7]}")

print(resultado[0][0])
print("=="*30)
print("\n")

# Consulta filtrada

cursor.execute("SELECT * FROM CadastroCliente WHERE cpf = '100.100.100-10'") # Aqui vai retornar apenas os cpfs que contem essa numeração "000.000.000-00"
resultado = cursor.fetchall()

print("CPF de Thamara Araújo:\n")

for c in resultado:
    print(f"ID: {c[0]}, Cliente: {c[1]}, Idade: {c[2]}, CPF: {c[3]}, E-mail: {c[4]}, Endereço: {c[5]}, Sexo: {c[6]}, Salário: {c[7]}")
print(resultado[0][0])

print("=="*30)
print("\n")

# Continuação 16.10.2025
# Realizando atualização no cadastro do cliente

cursor.execute("UPDATE CadastroCliente SET email = 'letticiaeugenio@email.com' WHERE id = 1")
cursor.execute("SELECT * FROM CadastroCliente") # Aqui vai retornar apenas os cpfs que contem essa numeração "000.000.000-00"
resultado = cursor.fetchall()
con.commit()

print("\nE-mail atualizado com sucesso!\n")


for e in resultado:
    print(f"ID: {e[0]}, Cliente: {e[1]}, Idade: {e[2]}, CPF: {e[3]}, E-mail: {e[4]}, Endereço: {e[5]}, Sexo: {e[6]}, Salário: {e[7]}")
print(resultado[0][0])
print("=="*30)
print("\n")




# Deletando cliente de id = 7 da base de dados

cursor.execute("DELETE FROM CadastroCliente WHERE id = 7")
cursor.execute("SELECT * FROM CadastroCliente") # Aqui vai retornar apenas os cpfs que contem essa numeração "000.000.000-00"
resultado = cursor.fetchall()
con.commit()

print("\nCliente deletado com sucesso!\n")
print(resultado[0][0])
print("=="*30)
print("\n")


# Organizando os dados segundo uma coluna escolhida - ORDER GROUP

cursor.execute("SELECT endereço, COUNT(id) AS NumeroDeClientes FROM CadastroCliente GROUP BY endereço")
# cursor.execute("SELECT * FROM CadastroCliente") # Aqui vai retornar apenas os cpfs que contem essa numeração "000.000.000-00"
resultado = cursor.fetchall()


print("\nQuantidade de clientes em casa cidade:")

# for r in resultado:
#     print(f"Cliente: {r[1]}, Endereço: {r[5]}")

print(resultado[0][0])
print("=="*30)
print("\n")


con.commit() # Grava a tabela
con.close() # Fecha a conexão


