from datetime import date
import functools # Importando o modulo functools da biblioteca padrão do Python

def safe_run(func):
  """Decorator para prooteger funções contra erros inesperados"""

  @functools.wraps(func)
  def wrapper(*args, **kwargs):

    try: 

      return func(*args, **kwargs) # Tenta executar a função original
    
    except Exception as e: # Se qualquer erro acontecer no try, capture esse erro (Exception) e coloque ele dentro da variável e, para eu poder usar depois

      print(f"[ERRO INESPERADO] Falha de execução na função '{func.__name__}'. Erro capturado: {e}")

      return None # Impede a aplicação de quebrar
    
  return wrapper # faz com que a função original seja substituída pela função “decorada”, com a lógica extra aplicada

"""Teste de Implementação"""

@safe_run
def servico_falho(data):
  """Simula um serviço que pode falahar em um cenário minoritário."""
  if data is None: 
    raise Exception("Dados de entrada não podem ser None. Simulação de falha de serviço externo.")
  return f"Resultado bem-sucedido com dados: {data.upper()}"

@safe_run
def servico_sucess():
  """Um serviço que calcula a soma, mas que pode ser decorado para segurança."""

  if y == 0:
    # Exemplo de falha interna
    return x / y
  return  x + y

""" Função quebrada para teste"""

@safe_run
def funcao_quebrada():
  raise Exception("Falha proposital para testar o safe_run!")

""" Testando """

resultado = funcao_quebrada()
print("Resultado da função:", resultado)

## Teste de Sucesso (Cenário 1)
print("\n--- Teste 1: Sucesso ---")
resultado_sucesso = servico_falho("teste ok")
print(f"Resultado da função (Sucesso): **{resultado_sucesso}**")

## Teste de Falha (Cenário 2)
print("\n--- Teste 2: Falha Controlada ---")
resultado_falha = servico_falho(None)
print(f"Resultado da função (Falha): **{resultado_falha}**")

## Teste de Falha (Cenário 3: Exceção nativa)
print("\n--- Teste 3: Divisão por Zero ---")
# A função irá tentar executar 10/0, gerando um ZeroDivisionError
resultado_divisao = servico_sucess(10, 0)
print(f"Resultado da função (Divisão por Zero): **{resultado_divisao}**")