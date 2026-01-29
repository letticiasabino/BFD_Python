class Calculadora:
  def somar(self, a, b):
    return a + b
  
  def subtrair(self, a, b):
    return a - b
  
  def multiplicar(self, a, b):
    return a * b
  
  def dividir(self, a, b):
    if b == 0:
      raise ValueError("Não é possível dividir por zero.")
    return a / b
  
if __name__ == "__main__":
  calc = Calculadora()

  print("--- Teste Manual da Calculadora ---")

# Testando 

  print(f"Soma (10 + 5): {calc.somar(10, 5)}")
  print(f"Subtração (20 + 9): {calc.subtrair(20, 9)}")
  print(f"Multiplicação (6 * 6): {calc.multiplicar(6, 6)}")
  print(f"Divisão (50 / 2): {calc.dividir(50, 2)}")