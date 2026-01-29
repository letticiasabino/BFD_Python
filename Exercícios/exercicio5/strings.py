''' texto = "Curso Back End Python" 

print(texto.lower())
print(texto.capitalize())
print(texto.upper())
print(texto.title())
print(texto.strip(' '))
print(texto.lstrip())
print(texto.rsplit())
print(texto.replace("Curso","Aulas de")) 
# "Curso" in texto
print(texto.find("Python"))
print(texto.index(''))
print(texto.startswith(""))
print(texto.endswith(""))
print(texto.split('-'))
novo_texto = texto.split("-")
print(novo_texto)
texto_novo = "-".join(novo_texto)
print(texto_novo)

curso = "Python"

dia = "Terças e quintas"

num_dec = 0.50405094

print(f'O curso de {curso} acontece as {dia}, {num_dec:0.2f}')

texto = "Olá, fração, decoding"

b_utf = texto.encode('utf-8')

print(b_utf)

texto_decodificado = b_utf.decode('utf-8')

print(texto_decodificado)'''