import unittest
from unittest.mock import patch
import cadastro

class TestCadastro(unittest.TestCase):

  # Teste de nome

  @patch('builtins.input', return_value='Letticia')
  def test_ler_nome_valido(self, mock_input):
    self.assertEqual(cadastro.ler_nome(), 'Letticia')

  @patch('builtins.input', return_value='12345')
  def test_ler_nome_invalido(self, mock_input):
    with self.assertRaises(ValueError):
      cadastro.ler_nome()

# Teste Sobrenome
  @patch('builtins.input', return_value='Sabino')
  def test_ler_sobrenome_valido(self, mock_input):
    self.assertEqual(cadastro.ler_sobrenome(), 'Sabino')

  @patch('builtins.input', return_value='     ')
  def test_ler_sobrenome_invalido(self, mock_input):
    with self.assertRaises(ValueError):
      cadastro.ler_sobrenome()

  # Teste de sexo
  @patch('builtins.input', return_value='f')
  def test_ler_sexo_feminino(self, mock_input):
    self.assertEqual(cadastro.ler_sexo(), 'F')

  @patch('builtins.input', return_value='X')
  def test_ler_sexo_invalido(self, mock_input):
    with self.assertRaises(ValueError):
      cadastro.ler_sexo()

  # Teste de Endereço
  @patch('builtins.input', return_value='Rua das Flores, 123')
  def test_ler_endereco_valido(self, mock_input):
    self.assertEqual(cadastro.ler_endereco(), 'Rua das Flores, 123')

  @patch('builtins.input', return_value='Rua')
  def test_ler_endereco_curto(self, mock_input):
    with self.assertRaises(ValueError):
      cadastro.ler_endereco()

  # Teste de Idade
  @patch('builtins.input', return_value='25')
  def test_ler_idade_valida(self, mock_input):
    self.assertEqual(cadastro.ler_idade(), 25)

  @patch('builtins.input', return_value='duzentos')
  def test_ler_idade_texto(self, mock_input):
    with self.assertRaises(ValueError):
      cadastro.ler_idade()

  # Testes de E-mail
  @patch('builtins.input', return_value='letticia@gmail.com')
  def test_ler_email_valido(self, mock_input):
    self.assertEqual(cadastro.ler_email(), 'letticia@gmail.com')

  @patch('builtins.input', return_value='emailsemarroba.com')
  def test_ler_email_invalido(self, mock_input):
    with self.assertRaises(ValueError):
      cadastro.ler_email()

if __name__ == '__main__':
  unittest.main()