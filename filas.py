"""
O Sr. Joaquim tem um restaurante muito popular é preciso de ajuda para gerir a fila de espera dos clientes.
Pretende-se criar um programa para registar os nomes dos clientes em espera e de cada vez retirar 
o primeiro a chegar á fila de espera(FIFO)
Menu : 1.Entrada 2.Saída 3.Consultar Fila 4.Terminar
"""
import numpy as np

NR_MAX = 10

def Entrada(fila):
    """Adicionar um nome ao final da fila de espera"""
    # Procurar o ultimo lugar da fila
    encontrou = False
    for posicao in range(NR_MAX):
        if fila[posicao] == "":
            encontrou = True
            break
    # Avisar se a fila esta cheia
    if encontrou == False:
        print("Fila cheia. Volte mais tarde.")
        return
    #ler o nome
    nome = input("Insira o nome para a fila de espera: ")
    # Inserir no final da fila
    fila[posicao] = nome
    print(f"A sua posição na fila de espera é {posicao+1}ª")

def Saida(fila):
    """retirar o primeiro nome na fila de espera"""
    # Verificar se a fila está vazia
    if fila[0] == "":
        print("A fila está vazia. ")
        return
    # Retirar o primeiro nome da fila
    print(f"O cliente com o nome {fila[0]} pode entrar.")
    # avançar os restantes nomes da fila uma posição
    for i in range(NR_MAX-1):
        fila[i] = fila[i+1]

    fila[NR_MAX-1] == "" # Para limpar a última posição do array
def ConsultarFila(fila):
    """Listar os nomes da fila de espera"""
    # verificar se a fila está vazia
    if fila[0] == "":
        print("A fila está vazia. ")
        return
    # Listar os nomes das pessoas em espera
    Fila_cheia = True
    for posicao in range(NR_MAX):
        if fila[posicao] == "":
            Fila_cheia = False
            break       
        print(f"{posicao+1}º - {fila[posicao]}")
    # verificar se a fila está cheia
    if Fila_cheia == True:
        print("Fila de espera está cheia.")

def Main():
    fila = np.empty(NR_MAX,dtype="U20")
    # limpar o array
    for i in range(NR_MAX):
        fila[i] = ""

    Op = 0
    while Op != 4:
        print("""
Menu :  1.Entrada 
        2.Saída 
        3.Consultar Fila 
        4.Terminar
""")
        Op = input("Opção: ")
        if Op == "1":
            Entrada(fila)
        elif Op == "2":
            Saida(fila)
        elif Op == "3":
            ConsultarFila(fila)
        elif Op == "4":
            break
        else:
            print("Opção inválida")

if __name__=="__main__":
    Main()