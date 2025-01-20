texto = "olá mundo"

tamanho = len(texto)
print(tamanho)

texto = texto.upper() # devolve a string em maiulculas
print(texto)

texto = texto.lower() # devolve a string em minusculas
print(texto)

texto = texto.capitalize() # devolve a string com a primeira letra maiuscula
print(texto)

texto = texto.strip() # devolve a string sem espaços em branco no INICIO E NO FINAL
print(texto)

texto = texto.replace(" ","-") # devolve a string substituindo o primeiro parametro pelo segundo
print(texto)

print(texto.isdigit()) # devolve verdadeiro se a string tiver numeros se tiver as letras sem digitos(numeros) devolve false

frase = "Olá mundo, o computador é uma torradeira"

palavras = frase.split(" ") # devolve uma lista com as partes da string separadas por caracteres indicados
print(palavras)
print(len(palavras))
print(palavras[0])

posicao = frase.index("a") # devolve a posição da string mas se nao existir da erro
print(posicao)

posicao = frase.find("m") # devolve a posição da string se não devolve -1

if posicao == -1:
    print("Não encontrei")
else:
    print("Encontrei na posição "+str(posicao))

# codigo ascii de uma letra
codigo = ord('a')
print(codigo)

#devolve a letra correspondente ao codigo ascii
letra = chr(97)

print(letra)


