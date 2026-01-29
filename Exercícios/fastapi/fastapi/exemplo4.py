"""
Agora vamos restringir o que pode ser enviado seguindo um modelo com pydantic
Vamos simular o envio destes dados nos baseando nos tipos que o modelo fornece.

"""

from fastapi import FastAPI
from pydantic import BaseModel

class Produto(BaseModel):
    nome: str
    preco: float
    promo: bool = False
    quant: int

app = FastAPI() 

@app.post("/produtos/") #Como vai existir um modelo a ser obedecido, não pedimos por parâmetros na URL.
def cadastro_produto(produto: Produto): #Reparem a utilização da classe produto como restrição, só isso ja é necessário para validar.
    
    #Aqui dentro podemos olhar para todas as infos do modelo:
    nome = produto.nome
    preco = produto.preco
    promo = produto.promo
    quant = produto.quant

    #como estes dados não estão sendo salvos, vamos retornar numa lista apenas para ver o resultado.
    return [nome,preco,promo,quant]
    #outra opção seria: return [produto.nome, produto.preco,...]
