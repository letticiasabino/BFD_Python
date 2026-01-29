"""
Agora que já entendemos o básico de como os testes funcionam, vamos utilizar o módulo que o python nos fornece para realizar testes.
"""

import unittest
from fibo import fibonacci
from rstrings import rstrings
import string

class TestFibo(unittest.TestCase): #Vamos herdar nossa classe de testes!

    def Setup(self):
        pass

    def test_len_fibo(self):
        #Aqui iremos testar se a quantidade de valores retornada está vindo corretamente.
        resultado = [i for i in fibonacci(9)]
        self.assertEqual(len(resultado),9) #assertEqual irá conferir se os resultados são iguais, temos várias outras opções de assert!

    def test_position_fibo(self):
        #Neste teste iremos conferir se o valor está correto de acordo com a posição da sequência fibonacci.
        pos_cinco = 8 #Sabemos que partindo do 0, a posição 5 tem que ser igual a 8!
        
        resultado = [i for i in fibonacci(5)]

        self.assertEqual(pos_cinco,resultado[-1])
        
class TestRstrings(unittest.TestCase):
    """Teste para verificar a integridade da nossa função de gerar strings aleatórias"""
    
    gerador = rstrings()

    def Setup(self):
      pass 

    def test_len_rstrings(self):
        
        letras = self.gerador.letras(15)
        l_n = self.gerador.l_n(15)
        
        self.assertEqual(len(letras),15)
        
        self.assertEqual(len(l_n),15)
        
    def test_simbols_rstrings(self):
        
        resultado = self.gerador.l_n(15)

        self.assertNotIn(resultado,string.punctuation)
        

if __name__ == '__main__':
    unittest.main()