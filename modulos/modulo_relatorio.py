import os
from time import sleep
relatorios = {}
def menu_relatorio(clientes, bicicletas, capacetes, sapatilhas, roupas, vendas):
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
        try:
            q = int(input('Qual opção você deseja: '))
        except ValueError:
            print('Entrada inválida! Por favor, escolha um número de 1 a 4.')
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
                try:
                    resp = int(input('Digite a opção que deseja: '))
                except ValueError:
                    print('Entrada inválida! Por favor, escolha um número de 1 a 5.')
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
                        
        if q == 2: 
            resp = ' '
            while resp != 6:
                print('''
#######################################
###      RELATÓRIO  PRODUTOS        ###
#######################################
# 1 - LISTAR PRODUTOS POR CATEGORIA   #
# 2 - LISTAR PRODUTOS ATIVOS          #
# 3 - LISTAR PRODUTOS DESATIVADOS     #
# 4 - PESQUISAR PRODUTOS              #
# 5 - PESQUISAR PRODUTOS PELO PREÇO   #
# 6 - SAIR                            #
                      ''')
                try:
                    resp = int(input('Qual opção você deseja: '))
                except ValueError:
                    print('Entrada inválida! Por favor, escolha um número de 1 a 6.')
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
                        try:
                            q = int(input('Qual opção você deseja: '))
                        except ValueError:
                            print('Entrada inválida! Por favor, escolha um número de 1 a 5.')
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
                        try:
                            q = int(input('Qual opção você deseja: '))
                        except ValueError:
                            print('Entrada inválida! Por favor, escolha um número de 1 a 5')
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
                        try:
                            q = int(input('Qual opção você deseja: '))
                        except ValueError:
                            print('Entrada inválida! Por favor, escolha um número de 1 a 5.')
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

                if resp == 4:
                    q = ''
                    while q != 5:
                        print('''
####################################
###         MENU PESQUISA        ###
####################################
# 1 - PESQUISAR BICICLETAS         #
# 2 - PESQUISAR CAPACETES          #
# 3 - PESQUISAR SAPATILHAS         #
# 4 - PESQUISAR ROUPAS             #
# 5 - SAIR                         #
                              ''')
                        try:
                            q = int(input('Qual opção você deseja ?'))
                        except ValueError:
                            print('Entrada inválida! Por favor, escolha um número de 1 a 5.')
                        if q == 1:
                            p = input('Digite o modelo da bicicleta: ').strip().upper()
                            print('Pesquisando no estoque...')
                            sleep(2)
                            for codigo in bicicletas:
                                if bicicletas[codigo][1].upper().startswith(p):
                                    print('--------------------')
                                    print('Codigo:', codigo)
                                    print('Marca:', bicicletas[codigo][0])
                                    print('Modelo:', bicicletas[codigo][1])
                                    print('Valor:', bicicletas[codigo][2])
                                    print('Quantidade:', bicicletas[codigo][3])
                                    print('Status', bicicletas[codigo][4])
                        if q == 2:
                            p = input('Digite o modelo do capacete: ').strip().upper()
                            print('Pesquisando no estoque...')
                            sleep(2)
                            for codigo in capacetes:
                                if capacetes[codigo][1].upper().startswith(p):
                                    print('--------------------')
                                    print('Codigo:', codigo)
                                    print('Marca:', capacetes[codigo][0])
                                    print('Modelo:', capacetes[codigo][1])
                                    print('Valor:', capacetes[codigo][2])
                                    print('Quantidade:', capacetes[codigo][3])
                                    print('Status', capacetes[codigo][4])
                            
                        if q == 3:
                            p = input('Digite o modelo do sapatilha: ').strip().upper()
                            print('Pesquisando no estoque...')
                            sleep(2)
                            for codigo in sapatilhas:
                                if sapatilhas[codigo][1].upper().startswith(p):
                                    print('--------------------')
                                    print('Codigo:', codigo)
                                    print('Marca:', sapatilhas[codigo][0])
                                    print('Modelo:', sapatilhas[codigo][1])
                                    print('Valor:', sapatilhas[codigo][2])
                                    print('Quantidade:', sapatilhas[codigo][3])
                                    print('Status', sapatilhas[codigo][4])
                                
                        if q == 4:
                            p = input('Digite a marca da roupa: ').strip().upper()
                            print('Pesquisando no estoque...')
                            sleep(2)
                            for codigo in roupas:
                                if roupas[codigo][0].upper().startswith(p):
                                    print('--------------------')   
                                    print('Codigo:', codigo)
                                    print('Marca:', roupas[codigo][0])
                                    print('Modelo:', roupas[codigo][1])
                                    print('Valor:', roupas[codigo][2])
                                    print('Quantidade:', roupas[codigo][3])
                                    print('Status', roupas[codigo][4])
                if resp == 5:
                    q = ''
                    while q != 5:
                        print('''
####################################
###      PESQUISA POR PREÇOS     ###
####################################
# 1 - PREÇO BICLETAS               #
# 2 - PREÇO CAPACETES              #
# 3 - PREÇO SAPATILHAS             #
# 4 - PREÇO ROUPAS                 #
# 5 - SAIR                         #
                              ''')
                        try:
                            q = int(input('Qual opção você deseja ?'))
                        except ValueError:
                            print('Entrada inválida! Por favor, escolha um número de 1 a 5.')
                        if q == 1:
                            p = int(input('Informe o valor desejado: '))
                            for codigo in bicicletas:
                                if bicicletas[codigo][2] <= p:
                                    print('--------------------')
                                    print('Codigo:', codigo)
                                    print('Marca:', bicicletas[codigo][0])
                                    print('Modelo:', bicicletas[codigo][1])
                                    print('Valor:', bicicletas[codigo][2])
                                    print('Quantidade:', bicicletas[codigo][3])
                                    print('Status', bicicletas[codigo][4])
                        if q == 2:
                            p = int(input('Informe o valor desejado: '))
                            for codigo in capacetes:
                                if capacetes[codigo][2] <= p:
                                    print('--------------------')
                                    print('Codigo:', codigo)
                                    print('Marca:', capacetes[codigo][0])
                                    print('Modelo:', capacetes[codigo][1])
                                    print('Valor:', capacetes[codigo][2])
                                    print('Quantidade:', capacetes[codigo][3])
                                    print('Status', capacetes[codigo][4])
                        if q == 3:
                            p = int(input('Informe o valor desejado: '))
                            for codigo in sapatilhas:
                                if sapatilhas[codigo][2] <=p:
                                    print('--------------------')
                                    print('Codigo:', codigo)
                                    print('Marca:', sapatilhas[codigo][0])
                                    print('Modelo:', sapatilhas[codigo][1])
                                    print('Valor:', sapatilhas[codigo][2])
                                    print('Quantidade:', sapatilhas[codigo][3])
                                    print('Status', sapatilhas[codigo][4])
                        if q == 4:
                            p = int(input('Informe o valor desejado: '))
                            for codigo in roupas:
                                if roupas[codigo][2] <= p:
                                    print('--------------------')   
                                    print('Codigo:', codigo)
                                    print('Marca:', roupas[codigo][0])
                                    print('Modelo:', roupas[codigo][1])
                                    print('Valor:', roupas[codigo][2])
                                    print('Quantidade:', roupas[codigo][3])
                                    print('Status', roupas[codigo][4])
        if q == 3:
            resp = ''
            while resp != 7:
                print('''
#######################################
###        RELATÓRIO  VENDAS        ###
#######################################
# 1 - LISTAR VENDAS                   #
# 2 - FATURAMENTO TOTAL DO MÊS        #
# 3 - LISTAR VENDAS POR PAGAMENTO     #
# 4 - LISTAR VENDAS POR VALOR         #
# 5 - LISTAR VENDAS POR CLIENTES      #
# 6 - LISTAR VENDAS POR PRODUTOS      #
# 7 - SAIR                            #
                      ''')
                try:
                    resp = int(input('Qual opção você deseja: '))
                except ValueError:
                    print('Entrada inválida! Por favor, escolha um número de 1 a 7.')
                if resp == 1:
                    q = ''
                    while q != 4:
                        print('''
################################
# 1 - LISTAR TODAS AS VENDAS   #
# 2 - LISTAR VENDAS ATIVAS     #
# 3 - LISTAR VENDAS CANCELADAS #
# 4 - SAIR
                              ''')
                        try:
                            q = int(input('Qual opção você deseja: '))
                        except ValueError:
                            print('Entrada inválida! Por favor, escolha um número de 1 a 4.')
                        if q == 1:
                            print('Listando todas as vendas...')
                            sleep(2)
                            for cod_venda in vendas:
                                    print('------------------------')
                                    print('Código da Venda:', cod_venda)
                                    print('Cliente:', vendas[cod_venda][0])
                                    print('Código Cliente:', vendas[cod_venda][1])
                                    print('Produto:', vendas[cod_venda][2])
                                    print('Código Produto:', vendas[cod_venda][3])
                                    print('Valor: R$', vendas[cod_venda][4])
                                    print('Pagamento:', vendas[cod_venda][5])
                                    print('Data/Hora:', vendas[cod_venda][6])
                                    print('Status:', vendas[cod_venda][7])
                        if q == 2:
                            print('Listando apenas vendas ativas...')
                            sleep(2)
                            for cod_venda in vendas:
                                if vendas[cod_venda][7] == 'ATIVA':
                                    print('------------------------')
                                    print('Código da Venda:', cod_venda)
                                    print('Cliente:', vendas[cod_venda][0])
                                    print('Código Cliente:', vendas[cod_venda][1])
                                    print('Produto:', vendas[cod_venda][2])
                                    print('Código Produto:', vendas[cod_venda][3])
                                    print('Valor: R$', vendas[cod_venda][4])
                                    print('Pagamento:', vendas[cod_venda][5])
                                    print('Data/Hora:', vendas[cod_venda][6])
                                    print('Status:', vendas[cod_venda][7])
                        if q == 3:
                            print('Listando apenas as vendas canceladas...')
                            sleep(2)
                            for cod_venda in vendas:
                                if vendas[cod_venda][7] == 'CANCELADA':
                                    print('------------------------')
                                    print('Código da Venda:', cod_venda)
                                    print('Cliente:', vendas[cod_venda][0])
                                    print('Código Cliente:', vendas[cod_venda][1])
                                    print('Produto:', vendas[cod_venda][2])
                                    print('Código Produto:', vendas[cod_venda][3])
                                    print('Valor: R$', vendas[cod_venda][4])
                                    print('Pagamento:', vendas[cod_venda][5])
                                    print('Data/Hora:', vendas[cod_venda][6])
                                    print('Status:', vendas[cod_venda][7])
                        
                if resp == 2:
                    faturamento = 0
                    for cod_venda in vendas:
                        if vendas[cod_venda][7] == 'ATIVA':
                            faturamento += vendas[cod_venda][4]
                    print(f'O faturamento total da loje nesse mês foi de R${faturamento:.2f}')

                if resp == 3:
                    q = ' '
                    while q != 4:
                        print('''
###############################
# 1 - VENDAS PIX              #
# 2 - VENDAS ESPÉCIE          #
# 3 - VENDAS CARTÃO           #
# 4 - SAIR                    #
                              ''')
                        try:
                            q = int(input('Qual opção você deseja: '))
                        except ValueError:
                            print('Entrada inválida! Por favor, escolha um número de 1 a 4.')
                        if q == 1:
                            print('Listando as vendas com pagamento pelo PIX')
                            for cod_venda in vendas:
                                if vendas[cod_venda][5] == 'PIX':
                                    print('------------------------')
                                    print('Código da Venda:', cod_venda)
                                    print('Cliente:', vendas[cod_venda][0])
                                    print('Código Cliente:', vendas[cod_venda][1])
                                    print('Produto:', vendas[cod_venda][2])
                                    print('Código Produto:', vendas[cod_venda][3])
                                    print('Valor: R$', vendas[cod_venda][4])
                                    print('Pagamento:', vendas[cod_venda][5])
                                    print('Data/Hora:', vendas[cod_venda][6])
                                    print('Status:', vendas[cod_venda][7])
                        if q == 2:
                            print('Listando as vendas com pagamento em ESPÉCIE')
                            for cod_venda in vendas:
                                if vendas[cod_venda][5] == 'ESPÉCIE':
                                    print('------------------------')
                                    print('Código da Venda:', cod_venda)
                                    print('Cliente:', vendas[cod_venda][0])
                                    print('Código Cliente:', vendas[cod_venda][1])
                                    print('Produto:', vendas[cod_venda][2])
                                    print('Código Produto:', vendas[cod_venda][3])
                                    print('Valor: R$', vendas[cod_venda][4])
                                    print('Pagamento:', vendas[cod_venda][5])
                                    print('Data/Hora:', vendas[cod_venda][6])
                                    print('Status:', vendas[cod_venda][7])
                        if q == 3:
                            print('Listando as vendas com pagamento no CARTÃO')
                            for cod_venda in vendas:
                                if vendas[cod_venda][5] == 'CARTÃO':
                                    print('------------------------')
                                    print('Código da Venda:', cod_venda)
                                    print('Cliente:', vendas[cod_venda][0])
                                    print('Código Cliente:', vendas[cod_venda][1])
                                    print('Produto:', vendas[cod_venda][2])
                                    print('Código Produto:', vendas[cod_venda][3])
                                    print('Valor: R$', vendas[cod_venda][4])
                                    print('Pagamento:', vendas[cod_venda][5])
                                    print('Data/Hora:', vendas[cod_venda][6])
                                    print('Status:', vendas[cod_venda][7])
                if resp == 4:
                    print('#### FILTRAR VENDAS POR VALOR ####')
                    v = int(input('Digite o valor R$: '))
                    print('Filtrando ...')
                    sleep(1)
                    print('Listando ...')
                    sleep(2)
                    for cod_venda in vendas:
                        if vendas[cod_venda][4] <= v:  
                            print('------------------------')
                            print('Código da Venda:', cod_venda)
                            print('Cliente:', vendas[cod_venda][0])
                            print('Código Cliente:', vendas[cod_venda][1])
                            print('Produto:', vendas[cod_venda][2])
                            print('Código Produto:', vendas[cod_venda][3])
                            print('Valor: R$', vendas[cod_venda][4])
                            print('Pagamento:', vendas[cod_venda][5])
                            print('Data/Hora:', vendas[cod_venda][6])
                            print('Status:', vendas[cod_venda][7])

                if resp == 5:
                    print('#### FILTRAR VENDAS POR CLIENTE ####')
                    c = input('Digite o código do cliente: ').upper()
                    print('Filtrando ...')
                    sleep(1)
                    print('Listando ...')
                    sleep(2)
                    for cod_venda in vendas:
                        if vendas[cod_venda][1] == c:
                            print('------------------------')
                            print('Código da Venda:', cod_venda)
                            print('Cliente:', vendas[cod_venda][0])
                            print('Código Cliente:', vendas[cod_venda][1])
                            print('Produto:', vendas[cod_venda][2])
                            print('Código Produto:', vendas[cod_venda][3])
                            print('Valor: R$', vendas[cod_venda][4])
                            print('Pagamento:', vendas[cod_venda][5])
                            print('Data/Hora:', vendas[cod_venda][6])
                            print('Status:', vendas[cod_venda][7])
                
                if resp == 6:
                    print('#### FILTRAR VENDAS POR PRODUTO ####')
                    c = input('Digite o código do produto: ')
                    print('Filtrando ...')
                    sleep(1)
                    print('Listando ...')
                    sleep(2)
                    for cod_venda in vendas:
                        if vendas[cod_venda][3] == c:
                            print('------------------------')
                            print('Código da Venda:', cod_venda)
                            print('Cliente:', vendas[cod_venda][0])
                            print('Código Cliente:', vendas[cod_venda][1])
                            print('Produto:', vendas[cod_venda][2])
                            print('Código Produto:', vendas[cod_venda][3])
                            print('Valor: R$', vendas[cod_venda][4])
                            print('Pagamento:', vendas[cod_venda][5])
                            print('Data/Hora:', vendas[cod_venda][6])
                            print('Status:', vendas[cod_venda][7])

    return relatorios