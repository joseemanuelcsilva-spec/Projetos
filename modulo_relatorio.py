import os
from time import sleep
relatorios = {}
def menu_relatorio(clientes, bicicletas, capacetes, sapatilhas, roupas):
    q = ' '
    while q != 4:
        print('''
#############################
####       MENU          ####
#############################
# 1 - RELATÓRIO DE CLIENTES #
# 2 - RELATÓRIO DE PRODUTOS #
# 3 - RELATÓRIO DE VENDAS   #
# 4 - SAIR                  #
               ''')
        q = int(input('Qual opção você deseja: '))
        if q == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            resp = ' '
            while resp != 5:
                print('''
##################################
###    RELATÓRIO  CLIENTES     ###
##################################
# 1 - LISTAR CLIENTES            #
# 2 - LISTAR CLIENTES ATIVOS     #
# 3 - LISTAR CLIENTES INATIVOS   #
# 4 - PESQUISAR CLIENTES         #
# 5 - SAIR                       #
                      ''')
                resp = int(input('Digite a opção que deseja: '))
                if resp == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Listando todos os clientes...')
                    sleep(2)
                    for cod in clientes:
                        print('-------------------------------------')
                        print('Codigo:', cod)
                        print('Nome:', clientes[cod][0])
                        print('Sobrenome:', clientes[cod][1])
                        print('Telefone:', clientes[cod][2])
                        print('CPF:', clientes[cod][3])
                        print('Status:', clientes[cod][4])
                if resp == 2:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Listando Clientes Ativos...')
                    sleep(2)
                    for cod in clientes:
                        if clientes[cod][4] == 'ATIVO':
                            print('-------------------------------------')
                            print('Codigo:', cod)
                            print('Nome:', clientes[cod][0])
                            print('Sobrenome:', clientes[cod][1])
                            print('Telefone:', clientes[cod][2])
                            print('CPF:', clientes[cod][3])
                            print('Status:', clientes[cod][4])
                
                if resp == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('Listando Clientes Desativados...')
                    sleep(2)
                    for cod in clientes:
                        if clientes[cod][4] == 'DESATIVADO':
                            print('-------------------------------------')
                            print('Codigo:', cod)
                            print('Nome:', clientes[cod][0])
                            print('Sobrenome:', clientes[cod][1])
                            print('Telefone:', clientes[cod][2])
                            print('CPF:', clientes[cod][3])
                            print('Status:', clientes[cod][4])
                if resp == 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    p = input('Digite o nome do cliente que deseja: ').strip().upper()
                    print('Listando...')
                    sleep(2)
                    for cod in clientes:
                        if clientes[cod][0].upper().startswith(p):
                            print('-------------------------------------')
                            print('Codigo:', cod)
                            print('Nome:', clientes[cod][0])
                            print('Sobrenome:', clientes[cod][1])
                            print('Telefone:', clientes[cod][2])
                            print('CPF:', clientes[cod][3])
                            print('Status:', clientes[cod][4])
                        
        if q == 2: #RELATÓRIO PRODUTOS
            resp = ' '
            while resp != 6:
                print('''
#######################################
###      RELATÓRIO  PRODUTOS        ###
#######################################
# 1 - LISTAR PRODUTOS POR CATEGORIA   #
# 2 - LISTAR PRODUTOS ATIVOS          #
# 3 - LISTAR PRODUTOS INATIVOS        #
# 4 - PESQUISAR PRODUTOS              #
# 5 - PESQUISAR PRODUTOS PELO PREÇO   #
# 6 - SAIR                            #
                      ''')
                resp = int(input('Qual opção você deseja: '))
                if resp == 1:
                    q = ''
                    while q != 5:
                        print('''
##################################
###         MENU PRODUTOS      ###
##################################
# 1 - LISTAR BICICLETAS          #
# 2 - LISTAR CAPACETES           #
# 3 - LISTAR SAPATILHAS          #
# 4 - LISTAR ROUPAS              #
# 5 - SAIR                       # 
                            ''')
                        q = int(input('Qual opção você deseja: '))
                        if q == 1:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            for codigo in bicicletas:
                                print('--------------------')
                                print('Codigo:', codigo)
                                print('Marca:', bicicletas[codigo][0])
                                print('Modelo:', bicicletas[codigo][1])
                                print('Valor:', bicicletas[codigo][2])
                                print('Quantidade:', bicicletas[codigo][3])
                                print('Status', bicicletas[codigo][4])
                        if q == 2:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            for codigo in capacetes: 
                                print('--------------------')
                                print('Código:', codigo)
                                print('Marca:', capacetes[codigo][0])
                                print('Modelo:', capacetes[codigo][1])
                                print('Valor:', capacetes[codigo][2])
                                print('Quantidade:', capacetes[codigo][3])
                                print('Status', capacetes[codigo][4])
                        if q == 3:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            for codigo in sapatilhas:
                                print('--------------------')
                                print('Codigo:', codigo)
                                print('Marca:', sapatilhas[codigo][0])
                                print('Modelo:',sapatilhas[codigo][1])
                                print('Valor:', sapatilhas[codigo][2])
                                print('Quantidade:', sapatilhas[codigo][3])
                                print('Status', sapatilhas[codigo][4])
                        if q == 4:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            for codigo in roupas:
                                print('--------------------')
                                print('Codigo:', codigo)
                                print('Marca:', roupas[codigo][0])
                                print('Tamanho:', roupas[codigo][1])
                                print('Valor:', roupas[codigo][2])
                                print('Quantidade:', roupas[codigo][3])
                                print('Status', roupas[codigo][4])
                if resp == 2:
                    q = ''
                    while q != 5:
                        print('''
##################################
###     PRODUTOS ATIVOS        ###
##################################
# 1 - BICICLETAS ATIVAS          #
# 2 - CAPACETES ATIVOS           #
# 3 - SAPATILHAS ATIVAS          #
# 4 - ROUPAS ATIVAS              #
# 5 - SAIR
                              ''')
                        q = int(input('Qual opção você deseja: '))
                        if q == 1:
                            for codigo in bicicletas:
                                if bicicletas[codigo][4] == 'ATIVO':
                                    print('--------------------')
                                    print('Codigo:', codigo)
                                    print('Marca:', bicicletas[codigo][0])
                                    print('Modelo:', bicicletas[codigo][1])
                                    print('Valor:', bicicletas[codigo][2])
                                    print('Quantidade:', bicicletas[codigo][3])
                                    print('Status', bicicletas[codigo][4])
                        if q == 2:
                            for codigo in capacetes:
                                if capacetes[codigo][4] == 'ATIVO':
                                    print('--------------------')
                                    print('Código:', codigo)
                                    print('Marca:', capacetes[codigo][0])
                                    print('Modelo:', capacetes[codigo][1])
                                    print('Valor:', capacetes[codigo][2])
                                    print('Quantidade:', capacetes[codigo][3])
                                    print('Status', capacetes[codigo][4])
                        if q == 3:
                            for codigo in sapatilhas:
                                if sapatilhas[codigo][4] == 'ATIVO':
                                    print('--------------------')
                                    print('Codigo:', codigo)
                                    print('Marca:', sapatilhas[codigo][0])
                                    print('Modelo:',sapatilhas[codigo][1])
                                    print('Valor:', sapatilhas[codigo][2])
                                    print('Quantidade:', sapatilhas[codigo][3])
                                    print('Status', sapatilhas[codigo][4])
                        if q == 4:
                            for codigo in roupas:
                                if roupas[codigo][4] == 'ATIVO':
                                    print('--------------------')
                                    print('Codigo:', codigo)
                                    print('Marca:', roupas[codigo][0])
                                    print('Tamanho:', roupas[codigo][1])
                                    print('Valor:', roupas[codigo][2])
                                    print('Quantidade:', roupas[codigo][3])
                                    print('Status', roupas[codigo][4])
                if resp == 3:
                    q = ''
                    while q != 5:
                        print('''
##################################
###    PRODUTOS DESATIVADOS    ###
##################################
# 1 - BICICLETAS DESATIVADAS     #
# 2 - CAPACETES DESATIVADOS      #
# 3 - SAPATILHAS DESATIVADAS     #
# 4 - ROUPAS DESATIVADAS         #
# 5 - SAIR                       #
                              ''')
                        q = int(input('Qual opção você deseja: '))
                        if q == 1:
                            for codigo in bicicletas:
                                if bicicletas[codigo][4] == 'DESATIVADO':
                                    print('--------------------')
                                    print('Codigo:', codigo)
                                    print('Marca:', bicicletas[codigo][0])
                                    print('Modelo:', bicicletas[codigo][1])
                                    print('Valor:', bicicletas[codigo][2])
                                    print('Quantidade:', bicicletas[codigo][3])
                                    print('Status', bicicletas[codigo][4])
                        if q == 2:
                            for codigo in capacetes:
                                if capacetes[codigo][4] == 'DESATIVADO':
                                    print('--------------------')
                                    print('Código:', codigo)
                                    print('Marca:', capacetes[codigo][0])
                                    print('Modelo:', capacetes[codigo][1])
                                    print('Valor:', capacetes[codigo][2])
                                    print('Quantidade:', capacetes[codigo][3])
                                    print('Status', capacetes[codigo][4])
                        if q == 3:
                            for codigo in sapatilhas:
                                if sapatilhas[codigo][4] == 'DESATIVADO':
                                    print('--------------------')
                                    print('Codigo:', codigo)
                                    print('Marca:', sapatilhas[codigo][0])
                                    print('Modelo:',sapatilhas[codigo][1])
                                    print('Valor:', sapatilhas[codigo][2])
                                    print('Quantidade:', sapatilhas[codigo][3])
                                    print('Status', sapatilhas[codigo][4])
                        if q == 4:
                            for codigo in roupas:
                                if roupas[codigo][4] == 'DESATIVADO':
                                    print('--------------------')
                                    print('Codigo:', codigo)
                                    print('Marca:', roupas[codigo][0])
                                    print('Tamanho:', roupas[codigo][1])
                                    print('Valor:', roupas[codigo][2])
                                    print('Quantidade:', roupas[codigo][3])
                                    print('Status', roupas[codigo][4]) 
    

        if q == 3:
            resp = ''
            resp = ' '
            while resp != 7:
                print('''
#######################################
###        RELATÓRIO  VENDAS        ###
#######################################
# 1 - LISTAR TODAS AS VENDAS          #
# 2 - FATURAMENTO TOTAL DO MÊS        #
# 3 - LISTAR VENDAS POR PAGAMENTO     #
# 4 - LISTAR VENDAS POR VALOR         #
# 5 - LISTAR VENDAS POR CLIENTES      #
# 6 - LISTAR VENDAS POR PRODUTOS      #
# 7 - SAIR                            #
                      ''')
                resp = int(input('Qual opção você deseja: '))

    return relatorios