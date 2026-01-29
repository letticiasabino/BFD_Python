import random
import string


class rstrings:
    """ Classe para gerar algumas strings randômicas"""
    
    def letras(self,len): 
        caracteres = string.ascii_letters

        resultado = "".join(random.choices(caracteres, k=len))

        return resultado
    
    def l_n(self,len):
        caracteres = string.ascii_letters + string.digits

        resultado = "".join(random.choices(caracteres,k=len))
        return resultado
    