class Aluno:
    def _init_(self, nome, gmail, turma, idade, nota):
        self.nome = nome
        self.gmail = gmail
        self.turma = turma
        self.idade = idade
        self.nota = nota
    def verificar_nota(self):
        return f"O aluno {self.nome} tem a nota {self.nota}"    

aluno1 = Aluno(nome = "Daniel", gmail = "aluno24@gmail.com", turma = "1241", idade = "16", nota = "7")  
aluno2 = Aluno(nome = "Gabriel", gmail = "aluno4324@gmail.com", turma = "1242", idade = "15" , nota="10")   

print(aluno2.verificar_nota)