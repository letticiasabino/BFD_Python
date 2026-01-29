""" Construa uma classe aluno, ela deve conter:
5 ATRIBUTOS
2 MÉTODOS """

class Aluno:
    def __init__(self, id, nome, nascimento, email, curso):
        self.id = id
        self.nome = nome
        self.nascimento = nascimento
        self.email = email
        self.curso = curso

    def verificarCurso(self):
        return f" Nome do Aluno: {self.nome}\n Curso: '{self.curso}'."
    
    def verificarCadastro(self):
        return f"Informações do Aluno: {self.nome}\n ID: {self.id}\n E-mail: {self.email}\n Data de Nascimento: {self.nascimento}"


Aluno1 = Aluno(id=1, nome="Vania Barros de Souza", nascimento="09/10/2003", email="vania@gmail.com", curso="Python")
Aluno2 = Aluno(id=2, nome="Felipe Brusse", nascimento="20/01/1999", email="felipe@gmail.com", curso="JAVA") 


print(f"Nome do Aluno 1: {Aluno1.nome}")
print(f"Nome do Aluno 2: {Aluno2.nome}")

print(Aluno1.verificarCurso())
print(Aluno2.verificarCurso())

print(Aluno1.verificarCadastro())
print(Aluno2.verificarCadastro())