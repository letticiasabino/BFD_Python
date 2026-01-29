"""
Para instalação:

        pip install fastapi[standard]

Existem versões do fastapi, é importante consultar a documentação. Vamos utilizar a padrão para essa aula.

O fastapi funciona semelhante ao django para rodar suas aplicações será necessário o comando no terminal:

        fastapi dev main.py

"""

from fastapi import FastAPI

app = FastAPI() #importação do fastapi


@app.get("/")    #Com este decorator declaramos a rota
def read_root(): #função para o endpoint existir
    return {"Hello": "World"} #o que ele irá retornar.


@app.get("/listas/nomes") #Podemos e devemos criar rotas para cada endpoint da nossa api.
def read_names():
    nomes = ["Fernanda","Brendo","Daniel","Adrielly","Letícia","Patrick","Júlia"]
    return nomes

@app.get("/listas/numeros")
def read_numbers():
    numeros = [10,20,30,40,50,60]
    return numeros + [70] #Tudo aqui dentro é python, lembrem-se! É possível fazer muito, não apenas ficar retornando!


"""
O fastapi cria automaticamente a documentação da api disponível em 2 rotas diferentes:

/docs
/redoc 

Recomendo muito a segunda opção!

confiram também o caminho:

/openapi.json
"""