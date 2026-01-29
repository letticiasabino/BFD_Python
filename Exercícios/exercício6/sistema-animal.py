# criando uma classe animal com atributos e metodos para emitir o som e depois mostrar as informacoes. 

class Animal:
  def __init__(self, nome, idade,tipo):
    self.nome = nome
    self.idade = idade
    self.tipo = tipo
    
  def emitir_som(self):
    print("Som genérico do animal!")
    
  def exibir_informacoes(self):
    print(f"Dados do animal:\nNome: {self.nome} | Idade: {self.idade} | Tipo: {self.tipo}")

# criando duas subclasses para mostrar na tela

class Cachorro(Animal):
  def emitir_som(self):
    print("Som canino: Au au!\n")

class Gato(Animal):
  def emitir_som(self):
    print("Som felino: Miau!\n")
    
# testando as classes 
cachorro1 = Cachorro("Foxy", 6, "Cachorro")
gato1 = Gato("Bunmi", 3, "Gato")

cachorro1.exibir_informacoes()
cachorro1.emitir_som()

gato1.exibir_informacoes()
gato1.emitir_som()

# criando uma lista vazia para armazenar os animais

animais = []

while True:
    print("\n=== Sistem ade Cadastro de Animais ===")
    print("1 - Cadastrar novo animal")
    print("2 - Mostrar todos os animais")
    print("3 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        tipo = input("Digite o tipo (Cachorro/Gato): ").capitalize()
        nome = input("Nome: ")
        idade = input("Idade: ")
    
        if tipo == "Cachorro":
            animal = Cachorro(nome, idade, tipo)
        
        elif tipo == "Gato":
            animal = Gato(nome, idade, tipo)
            
        else:
            print("Tipo inválido! Tente novamente.")
            
            continue
            
        animais.append(animal)
        print(f"{tipo} cadastrado com sucesso!")
            
    elif opcao == "2":
        if not animais:
            print("Nenhum animal cadastrado ainda.")
        else:
            for a in animais:
                a.exibir_informacoes()
                a.emitir_som()
                
    elif opcao == "3":
        print("Encerrando o sistema... Até logo!")
        break
    
    else:
        print("Opção inválidade! Tente novamente.")