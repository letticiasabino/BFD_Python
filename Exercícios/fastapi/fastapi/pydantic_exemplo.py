"""
pip install pydantic

Pydantic é uma biblioteca de validação de dados muito poderosa!
Ela é amplamente utilizada atualmente em todo ecosistema do python, recomendo pesquisarem melhor sobre ela:
O fastapi delega toda a validação de dados para o Pydantic, assim não precisamos fazer validações campo a campo
em JSONs que recebermos da web.
O Django também utiliza o Pydantic para validações!
Da pra notar a semelhança de validação com algumas estruturas presente no Django.
"""

from pydantic import BaseModel, PositiveInt, ValidationError
from datetime import datetime

class User(BaseModel): #É preciso herdar o BaseModel
    id: int
    name: str = 'Algum Nome'
    signup_ts : datetime | None    #A barra significa OR
    infos: dict[str, PositiveInt]


dados_externos = {'id':10,
                  'name':'Caio Marins',
                  'signup_ts': datetime.now(),
                  'infos':{'qualquer string':15}}

try:
    User(**dados_externos) #linha da verificação:
    
except ValidationError as e: #Caso algo dê errado
    print(e.errors())
