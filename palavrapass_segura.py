"""O programa vai verificar se a palavra pass é segura com base na tabela"""

import numpy as np
MR_password = 5

dicionario_password = np.array(["M3dia","12345","123456","password","admin"])

#for i in range(MR_password):
    #tabela = input("Insira as palavra pass proibidas: ")
    
palavrapass = input("Insira uma palavra pass: ")

if palavrapass in dicionario_password:
    print("A Palavra pass não é segura.")
else:
    print("A palavra pass é segura.")

