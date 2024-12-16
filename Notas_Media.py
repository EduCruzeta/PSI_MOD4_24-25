"""
Este programa vai ler as notas do utilizador e calcular a media ainda vai tambem 
cada vez que for maior que a media dizer se tem a cima da media ou nao
"""
import numpy as np

#constante com o valor do numero de alunos
NR_ALUNOS = 10

#definir o array para as notas
notas = np.zeros(NR_ALUNOS)

#ler as notas
for n in range(NR_ALUNOS):
    notas[n] = int(input(f"Introduza a nota do aluno nº {n+1}: "))

#calcular a média
soma = 0
for n in range(NR_ALUNOS):
    soma = soma + notas[n]

media = soma / NR_ALUNOS
print(f"A média das notas dos alunos foi de {media}")

#listar as notas são superiores à média
for n in range(NR_ALUNOS):
    if notas[n] > media:
        print(f"A nota {notas[n]} do aluno nº {n+1} é superior à média")
