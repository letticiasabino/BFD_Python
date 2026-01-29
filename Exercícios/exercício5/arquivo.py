class Pessoa:
    def __init__(self, nome, idade, email, senha):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.senha = senha

    def verificar_email(self):
       return f"A pessoa de nome: {self.nome} está cadastrado no email: '{self.email}'."
    
    def verificar_senha(self):
        return f"A senha da {self.nome} é: {self.senha}"
    
Pessoa1 = Pessoa(nome="Lettícia Sabino", idade=26, email="letticiaeugenio@gmail.com", senha="123456")
Pessoa2 = Pessoa(nome="Sara Gomes", idade=22, email="saragomes@gmail.com", senha="456789")
Pessoa3 = Pessoa(nome="Ytalo Araujo", idade=29, email="ytaloaraujo@gmail.com", senha="789456")

print(f"E-mail da Pessoa 1: {Pessoa2.email}")
print(f"Sua senha é: {Pessoa2.senha}")