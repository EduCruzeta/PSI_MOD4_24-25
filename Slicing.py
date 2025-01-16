"""
Slicing - Permite ter acesso a subconjuntos de uma sequência ou coleção
        sintaxe : sequencia[inicio:fim:passo]
        inicio - A posição do primeiro a incluir
        fim    - É a pisoção onde termina o slice NÃO É INCLUIDO
        passo  - Intervalo entre os elementos a incluir no slice
"""

nome = "Joaquim Silva"

nome_5_letras = nome[0:5:1]#----------# Copia as letras das posições 0 a 4

print(nome_5_letras)

nome_5_letras = nome[:5:1]#-----------# Copia as primeiras 5 letras

print(nome_5_letras)

nome_ultimas_letras = nome[7:]#-------# Copiar as letras da posição 7 ate ao fim

print(nome_ultimas_letras)

nome_ultimas_letras = nome[7:110]#----# Copiar as letras da posição 7 ate ao fim

print(nome_ultimas_letras)

nome_invertido = nome[::-1]#----------# Inverter uma string

print(nome_invertido)

nome_2_2_letras = nome[::2]

print(nome_2_2_letras)

print(nome[-1])#----------------------# Ultima letra da string

ultimo_nome_invertido = nome[12:7:-1] # Inverter o nome com indices positivos

print(ultimo_nome_invertido)

ultimo_nome_invertido = nome[-1:-6:-1]# Inverter o nome com indices negativos

print(ultimo_nome_invertido)

import numpy as np

nomes = np.array(["joaquim","maria","antónio","augusto","césar"])

# Mostrar todos os nomes por ordem inversa
    
print(nomes[5::-1])#------------------# ou print(nomes[-1::-1]) ou print(nomes[::-1])

# mostrar os dois ultimos nomes

print(nomes[3::])#--------------------# ou print(nomes[-2::]) ou print[len(nomes)-2:)]

# Mostrar o 1º 3º 5º

print(nomes[::2])