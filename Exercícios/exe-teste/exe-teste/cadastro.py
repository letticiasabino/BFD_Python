def ler_nome():
  nome = input("Digite seu nome: ")
  if not nome.isalpha():
    raise ValueError("O nome deve conter apenas letras.")
  return nome

def ler_sobrenome():
  sobrenome = input("Digite seu sobrenome: ")
  if not sobrenome.strip():
    raise ValueError("O sobrenome não pode estar vazio.")
  return sobrenome

def ler_sexo():
  sexo = input("Digite o seu sexo (M/F): ").upper()
  if sexo not in ['M', 'F']:
    raise ValueError("Sexo inválido. Use M ou F.")
  return sexo

def ler_endereco():
  endereco = input("Digite seu endereço: ")
  if len(endereco) < 5:
    raise ValueError("Endereço muito curto.")
  return endereco

def ler_idade():
  try:
    idade = int(input("Digite sua Idade: "))
    if idade < 0 or idade > 100:
      raise ValueError
    return idade
  except ValueError:
    raise ValueError("Idade inválida. Digite um número entre 0 e 100.")
  
def ler_email():
  email = input("Digite seu e-mail: ")
  if "@" not in email or '.' not in email:
    raise ValueError("E-mail inválido.")
  return email

# Função principal para rodar o projeto
def iniciar_cadastro():
  print("--- Cadastro de Usuuário ---")
  try:
    dados = {
      "nome": ler_nome(),
      "sobrenome": ler_sobrenome(),
      "sexo": ler_sexo(),
      "endereco": ler_endereco(),
      "idade": ler_idade(),
      "email": ler_email()
    }
    print("\nCadastro realizado com sucesso!")
    print(dados)
  except ValueError as e:
    print(f"Erro no cadastro: {e}")

if __name__ == "__main__":
  iniciar_cadastro()