import numpy as np
#------------------------------------------------------------#
#estrutura de dados
MAX_ITENS = 100
nomes = np.empty(MAX_ITENS,dtype="U50")
N_telefone = np.empty(MAX_ITENS,dtype="U9")
email = np.empty(MAX_ITENS,dtype="U50")
#------------------------------------------------------------#
def Menu():
    nr_contactos = 0
    nomes = np.empty(MAX_ITENS,dtype="U50")
    N_telefone = np.empty(MAX_ITENS,dtype="U9")
    email = np.empty(MAX_ITENS,dtype="U50")
    escolha = 0
    #Função responsavel por fazer o menu para o utilizador
    while escolha != 6:
        print("1.Adicioar\n2.Listar todos\n3.Procurar\n4.Apagar\n5.Editar\n 6.Terminar")
        escolha = int(input("Insira a sua escolha: "))
        if escolha == 1:
            nr_contactos = Adicionar(nomes,N_telefone,email,nr_contactos)
        elif escolha == 2:
            Listar_todos(nomes,N_telefone,email,nr_contactos)
        elif escolha == 3:
            Procurar(nomes,N_telefone,email,nr_contactos)
        elif escolha == 4:
            nr_contactos = Apagar(nomes,N_telefone,email,nr_contactos)
        elif escolha == 5:
            Editar(nomes,email,N_telefone,nr_contactos)
        elif escolha == 6:
            break
        else:
            print("escolha invalida!")
#------------------------------------------------------------#
def Adicionar(nomes,N_telefone,email,nr_contactos):
    """
    Esta função é responsavel por adidiconar os nomes email e telefones aos arrays.
    """
    print("#"*30)
    print("## A agenda de contactos está cheia!")
    print("#"*30)
    #testar se o array ja esta cheio
    if nr_contactos == MAX_ITENS:
        print("Erro exedeu o limite!")
        return nr_contactos

    nomes[nr_contactos] = input("Insira o nome: ")
    N_telefone[nr_contactos] = int(input("Insira o numero de telefone: "))
    email[nr_contactos] = input("Insira o email: ")
    print("-"*60)

    nr_contactos += 1

    return (nr_contactos)
#------------------------------------------------------------#
def Listar_todos(nomes,N_telefone,email,nr_contactos):
    print("#"*60)
    print("## Listar Contactos ",end="")
    print(" "*38,end="")
    print("##")
    print("#"*60)
    for i in range(nr_contactos):
        print(f"# {nomes[i]} \t {email[i]} \t {N_telefone[i]} \t #")

    print("-"*60)
#------------------------------------------------------------#    
def Procurar(nomes,N_telefone,email,nr_contactos):
    print("#"*60)
    print("## Procurar contactos ",end="")
    print(" "*38,end="")
    print("##")
    print("#"*60)
    nome_procurar = input("Qual o nome do contacto: ")
    for i in range(nr_contactos):
        if nome_procurar in nomes[i]:
            print(f"# {nomes[i]} \t {email[i]} \t {N_telefone[i]} \t #")
            op = input("Tem a certeza que pretende apagar este contacto? (s/n): ")
            if op in "sS":
                for k in range(i,nr_contactos):
                    if k == MAX_ITENS-1: #evita erro de passar o limite do array
                        break
                    nomes[k] = nomes[k+1]
                    N_telefone[k] = N_telefone[k+1]
                    nr_contactos[k] = nr_contactos[k+1]

                nr_contactos -=1
    
    return nr_contactos
#------------------------------------------------------------#
print("-"*60)
#------------------------------------------------------------#
def Editar(nomes,email,N_telefone,nr_contactos):
    """Função pesquisa um contacto pelo nome e permite alterar dados"""
    #pedir o nome ao utilizador
    nome = input("Qual o nome do contacto a editar: ")
    #precorrer o array dos nomes
    #encontrar o nome permite alterar os dados
    for i in range(nr_contactos):
        #encontrar o nome permite alterar os dados
        if nome in nomes[i]:
            print(f"Dados do contacto: {nomes[i]} - {email[i]} - {N_telefone[i]}")
            op = input("Pretende editar estes dados? (S/N)")
            if op.lower() != "s":
                continue
            #editar dados
            novo_nome = input("Introduza o novo nome ou deixa em branco para nao alterar: ")
            novo_email = input("Introduza o novo email ou deixa em branco para nao alterar: ")
            novo_telefone = input("Introduza o novo telefone ou deixa em branco para nao alterar: ")
            if novo_nome.strip() != "":
                nomes[i]=novo_nome.strip()
            if novo_email.strip() != "":
                nomes[i]=novo_email.strip()
            if novo_telefone.strip() != "":
                nomes[i]=novo_telefone.strip()
#------------------------------------------------------------#
def Apagar(nomes,N_telefone,email,nr_contactos):
    """
    Função para apagar da agenda o cadastro da pessoa
    """
    print("#"*60)
    print("## Procurar contactos ",end="")
    print(" "*38,end="")
    print("##")
    print("#"*60)
    nome_procurar = input("Qual o nome do contacto: ")
    for i in range(nr_contactos):
        if nome_procurar in nomes[i]:
            print(f"# {nomes[i]} \t {email[i]} \t {N_telefone[i]} \t #")
#------------------------------------------------------------#    
Menu()