def menu():
  print("==== SISTEMA DE CADASTRO ====")
  print("1. Cadastrar novo usuário")
  print("2. Ver usuários cadastrados")
  print("3. Sair")

def cadastrar_usuario():
  print("==== CADASTRO DE NOVO USUÁRIO ====")

  nome_completo = input("Nome completo: ")
  data_nascimento = input("Data de nascimento: ")
  local_nascimento = input("Local de nascimento: ")
  email = input("Email: ")
  telefone = input("Telefone: ")
  apelido = input("Apelido: ")
  senha = input("Senha: ")
  confirmacao_senha = input("Confirmação de senha: ")

  usuario = {
      "nome_completo": nome_completo,
      "data_nascimento": data_nascimento,
      "local_nascimento": local_nascimento,
      "email": email,
      "telefone": telefone,
      "apelido": apelido,
      "senha": senha
  }

  with open("usuarios.txt", "a") as arquivo:
    arquivo.write(str(usuario) + "\n")

  print("Usuário cadastrado com sucesso!")


def ver_usuarios():
  print("==== USUÁRIOS CADASTrados ====")
  with open("usuarios.txt", "r") as arquivo:
    usuarios = arquivo.readlines()
    for usuario in usuarios:
      print(usuario)


while True:
  menu()
  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    cadastrar_usuario()
    pass
  elif opcao == "2":
    ver_usuarios()
    pass
  elif opcao == "3":
    print("Saindo do sistema...")
    break
  else:
    print("Opção inválida. Tente novamente.")
    pass