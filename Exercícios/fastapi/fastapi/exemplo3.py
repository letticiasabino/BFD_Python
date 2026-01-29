"""
Até agora trabalhamos apenas com requisições get, mas apis também podem lidar com outras requisições.
GET é o padrão para retorno de informações.
"""

from fastapi import FastAPI

app = FastAPI() 

#Pequeno arquivo para persistência de dados
with open("nomes.txt","w+") as f:
    f.write("Nomes:\n")


#Vamos criar dados com requisição POST:

@app.post("/nomes/{name}")
def salva_nomes(name:str):

    with open("nomes.txt","+a") as f: #Abrindo o arquivo para escrever nele
        f.write(name.capitalize() + "\n")

    return "Salvo com sucesso!"

#Vamos recuperar dados com uma requisição GET
@app.get("/nomes/list_all")
def lista_nomes():
    with open("nomes.txt","r") as f: #Abrindo para ler o arquivo.
        nomes = f.readlines()

    return nomes