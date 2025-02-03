"""O progama vai ler as notas dos alunos nas disciplinas e vai calcular a media de cada um e a media da disciplina"""

import numpy as np

TAMANHO = (10,5)

matriz = np.zeros(TAMANHO,dtype="i")

for l in range(matriz.shape[0]):
    media = 0
    for c in range(matriz.shape[1]):
        matriz[l,c] = int(input(f"Insira o as notas do aluno {l+1} na {c+1} disciplinas: "))
        media = media + matriz[l,c]
    print(f"O {l+1} aluno tem media de {media/5}. ")

for c in range(matriz.shape[1]):
    mediaDisciplina = 0
    for l in range(matriz.shape[0]):
        mediaDisciplina = mediaDisciplina + matriz[l,c]
    print(f"A media da metéria nº {c+1} é de {mediaDisciplina/10}")
#------------------------------------------------------------------------------------------------------#

TAMANHO = (10,5)

notas = np.zeros(TAMANHO,dtype="i")

def LerDados(notas):
    """Função para precorrer as linhas e colunas da matriz notas e preencher com os dados inseridos pelo utilizador"""
    # ler as notas por aluno(linhas)
    for l in range(notas.shape[0]):
        for c in range(notas.shape[1]):
            notas[l,c] = input(f"Introduza a nota para o aluno Nº {l+1} na {c+1} disciplina: ")

def MediaPorAluno(notas):
    """Função para precorrer a matriz e calcular a média para cada um dos 10 alunos"""
    for l in range(notas.shape[0]):
        soma = 0
        for c in range(notas.shape[1]):
            soma = soma + notas[l,c]
        media = soma / notas.shape[1]
        print(f" A media do aluno {l+1} foi de {round(media,1)}")

def MediaPorDisciplina(notas):
    """Função para precorrer a matriz e calcular a média para cada uma das 5 disciplinas"""
    for c in range(notas.shape[1]):
        soma = 0
        for l in range(notas.shape[0]):
            soma = soma + notas[l,c]
        media = soma / notas.shape[0]
        print(f" A media da {c+1}º disciplina foi de {round(media,1)}")

