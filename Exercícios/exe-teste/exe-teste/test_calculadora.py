import unittest
from calculadora import Calculadora # Importa a classe do outro arquivo

class TestCalculadora(unittest.TestCase): # Precisa herdar de TestCase

  def setUp(self):
    # Essa função cria uma instância da calculadora antes de cada teste
    self.calc = Calculadora()

    # Teste de Soma
  def test_soma_positivos(self):
    self.assertEqual(self.calc.adicionar(10, 5), 15)

  def teste_soma_negativos(self):
      self.assertEqual(self.calc.adicionar(10, 5), 15)

  # Teste de Subtração
  def test_subtracao_simples(self):
      self.assertEqual(self.calc.subtrair(10, 5), 5)

  def test_subtracao_negativo(self):
      self.assertEqual(self.calc.subtrair(5, 10), -5)

  # Teste de Multiplicação
  def test_multiplicacao_padrao(self):
      self.assertEqual(self.calc.multiplicar(3, 4), 12)

  def test_multiplicacao_zero(self):
     self.assertEqual(self.calc.multiplicar(10, 0), 0)

  # Teste de Divisão
  def test_divisao_exata(self):
      self.assertEqual(self.calc.dividir(10, 2), 5)

  def test_divisao_quebrada(self):
      self.assertEqual(self.calc.dividir(10, 3), 3.3333333333333335)

  def test_divisao_zero(self):
   # Verifica se ValueError é levanntado
      with self.assertRaises(ValueError):
          self.calc.dividir(10, 0)

if __name__ == '__main__':
  unittest.main()