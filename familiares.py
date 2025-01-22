"""Programa para ler dois nomes completos e indicar se são familiares. Dois nomes são familiares se o ultimo 
nome for igual
Versão hacker: Dois nomes são de familiares se um dos ultimos nomes forem iguais por qualquer ordem 
(ultimo=penultimo, ultimo=ultimo, penultimo=penultimo.)"""

def Familiares(A,B) -> bool:
    """Função que devolve true se os nomes sao familiares"""
    nomesA = A.split(" ") # lista com os nomes
    nomesB = B.split(" ") # lista com os nomes
    #verificar se os últimos nomes são iguais
    if nomesA[len(nomesA)-1] == nomesB[len(nomesB)-1]:
        return True
    #verificar se os dois ultimos nomes são iguais
    for i in nomeA[1:]:
        for k in nomesB[1:]:
            if i == k:
                return True
    return False

nomeA = input("Introduza um nome completo: ")
nomeB = input("Introduza um nome completo: ")
if Familiares(nomeA,nomeB) == True:
    print("São familiares.")
else:
    print("Não são familiares.")
