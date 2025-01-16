"""
Um programa para registar os nomes dos clientes que entraram numa loja 
num determinado dia e o valor das compras de cada.
o programa deve mostrar o nome do cliente que fez a compra mais cara.
"""
import numpy as np

"""NR_CLIENTES = 5

nomes = np.zeros(NR_CLIENTES,dtype="U50")
compras = np.zeros(NR_CLIENTES,dtype="f")

for n in range(NR_CLIENTES):
    nomes[n] = input(f"Introduza o nome do cliente: ")
    compras[n] = int(input(f"Insira o preço das compras do cliente {nomes[n]}: "))

for i in range(NR_CLIENTES):
    maior = 0
    if compras[i] > maior:
        maior = compras[i]
        local = i

print(f"O cliente que fez a compra mais cara foi o senhor {nomes[local]} com o montante de {round(maior,2)}€")"""

#\-----------------------------------------------------------------------------------------------------------------/#

MAX_CLIENTES = 3

nomes_v2 = np.empty(MAX_CLIENTES,dtype="U50")
compras_v2 = np.empty(MAX_CLIENTES,dtype="f")

def Ler_dados(nomes_clientes,compras_clientes):
    #perguntar quantos clientes entraram
    n_clientes = int(input("Quantos clientes entraram na loja? "))
    for i in range(n_clientes):
        #ler nome
        nomes_clientes[i] = input("Nome: ")
        #ler o valor das compras
        compras_clientes[i] = input("Insira o valor das compras: ")

#Função para mostrar o nome do melhor cliente
def MelhorCliente(nomes_clientes,compras_clientes):
    posicao = 0
    #precorrer o array
    for i in range(MAX_CLIENTES):
        if compras_clientes[posicao] < compras_clientes[i]:
            #guardar o valor e a posição
            posicao = i

    print(f"O melhor cliente foi {nomes_clientes[posicao]} que gastou {compras_clientes[posicao]}€")

Ler_dados(nomes_v2,compras_v2)
MelhorCliente(nomes_v2,compras_v2)
