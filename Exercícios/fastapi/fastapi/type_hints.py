"""
Como já aprendemos anteriormente os typehints são utilizados em funções para marcar a tipagem de parâmetros
e o que ela deveria retornar. Para o python ela é apenas uma notação, para o fastapi ele é fundamental.
As anotações ajudaram a marcar os tipos reais dos dados, além de apenas uma notação de código.
Isso acontece pela utilização da biblioteca Pydantic para validação dos dados.
"""

def calc_preco(preco: float, desc: float) -> float:
    return preco - (preco * desc)

#O fastapi vai ler as typehints como assinaturas de tipos que cada parâmetro deve ter.

