"""
No exemplo 1 só retornamos nomes e números básicos, vamos ampliar os horizontes!
Vamos deixar que o usuário passe informações e vamos checar por elas.

"""

from fastapi import FastAPI

app = FastAPI() #importação do fastapi Não se esqueça!

@app.get("/nomes/{name}") #Com essa estrutura, um parâmetro deve ser passado a solicitação!
def checa_nome(name:str): #Obrigando a ser str!
    nomes = ["Fernanda","Brendo","Daniel","Adrielly","Letícia","Patrick","Júlia"]
    if name in nomes:
        return "O nome que você enviou existe aqui sim!!"
    else:
        return "Não conhecemos essa pessoa!"
    
@app.get("/numeros/{num}")
def soma(num: float):
    return num + (num/2)