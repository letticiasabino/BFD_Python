"""É possível escolher entre modelos possíveis para que um endpoint possa lidar com alguns tipos diferentes de entrada
Mas isso deve ser utilizado com cautela! """

from fastapi import FastAPI
from enum import Enum #Essa classe nos dará a possbilidade de enumerar os modelos
from pydantic import BaseModel

class ModelName(str, Enum):
    carro = "Carro"
    foo = "Foo"
    xpto = "Xpto"

app = FastAPI() 

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.carro:
        return {"model_name": model_name, "message": "Vruum Vruum"}

    if model_name.value == "Foo":
        return {"model_name": model_name, "message": "Foo Foo Foo Foo F00"}

    return {"model_name": model_name, "message": "XXXXXXXXXXXXXXXXXXXXXXXpto"}
