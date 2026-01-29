'''with open("arquivo.txt","w") as a:
    # Bloco de código que irá escrever no arquivo.
    a.write("Escrevo a primeira linha") # Write sobreescreve o arquivo'''

#with open("Letticia.txt","w") as a:
#    a .write("Linha um\n")
#    a .write("Linha dois\n")
#    a .write("Linha três\n")
#    a .write("Linha quatro\n")
#    a .write("Linha cinco\n")
#    a .writelines("Última linha!\n")
#
#with open("Letticia.txt","r") as r:
#    var = r.readlines()
#
#for i in var:
#    print(i)
#
#var.append("Conteúdo adicional")
#print(var)

#try:
#    var = int(input("Digite algum número: "))
#    print("Funciona!")
#
#except ValueError:
#    print("Digite um número inteiro: ")
#
#print("Continua")

def  testa_val(n):
    try:
        if n < 10:
            return 1
        else:
            return 0
    except ValueError:
        print("Erro")
        return -1
    finally:
        




#    print(r.read()) # Lê o arquivo 
#    print(r.readlines()) # Não repete a leitura, pois já leu no comando acima.

#with open("arquivo.txt","+a") as l:
#    l .write("Letticia\n")
#    l .write("Sabino\n")
#    l .write("da\n")
#    l .write("Conceicao\n")
#    l .write("Eugenio\n")
#    l .writelines("Nome completo!\n")
#print(l)