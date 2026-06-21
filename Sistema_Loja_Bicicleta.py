import os
from datetime import datetime
import time

from arquivos import salvar_bicicletas
from arquivos import salvar_capacetes
from arquivos import salvar_sapatilhas
from arquivos import salvar_roupas
from arquivos import salvar_clientes
from arquivos import salvar_vendas

from modulo_carregamento import carregar_bicicletas
from modulo_carregamento import carregar_capacetes
from modulo_carregamento import carregar_sapatilhas
from modulo_carregamento import carregar_roupas
from modulo_carregamento import carregar_clientes
from modulo_carregamento import carregar_vendas

from modulo_estoque import menu_estoque
from modulo_clientes import menu_clientes   

bicicleta = carregar_bicicletas()
capacete = carregar_capacetes()
sapatilha = carregar_sapatilhas()
roupa = carregar_roupas()
clientes = carregar_clientes()
vendas = carregar_vendas()

resp = ' '
while resp != 0:
        print('#'*31)
        print('##### Projeto - PedalFlow #####')
        print('#'*31)    
        print('''
###############################################
############ 1 - GERENCIAR ESTOQUE     ########
############ 2 - GERENCIAR CLIENTES    ########      
############ 3 - GERENCIAR VENDAS      ########     
############ 4 - RELATÓRIOS            ########
############ 5 - INFORMAÇÕES           ########
############ 0 - SAIR                  ########
                ''')
        resp = int(input('Qual opção você deseja: '))
        if resp == 1:
            menu_estoque()
        elif resp == 2:
            menu_clientes()


        elif resp == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
            q = ' '
            while q != 5:
                print('''
###############################################
############ 1 - NOVA VENDA            ########
############ 2 - HISTÓRICO DE VENDAS   ########      
############ 3 - BUSCAR VENDAS         ######## 
############ 4 - CANCELAR VENDA        ########    
############ 5 - VOLTAR                ########       
                    ''')
                q = int(input('Qual opção você deseja: '))
                agora = datetime.now()
                data_hora = agora.strftime("%d/%m/%Y %H:%M:%S")
                if q == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('#### VAMOS INCIAR UMA VENDA ####')
                    cod_cliente = input('Digite o código do cliente: ')
                    if cod_cliente in clientes: 
                        print('Cliente encontrado')
                        print(f"Seja bem vindo {clientes[cod_cliente][0]}")
                        while q != 5:
                            print('''
#############################
### O QUE DESEJA COMPRAR ?###    
#############################
### 1 - BICICLETA         ###
### 2 - SAPATILHA         ###
### 3 - CAPACETE          ###
### 4 - ROUPA             ###
### 5 - VOLTAR            ###
                            ''')
                            q = int(input('Digite a opção desejada: '))
                            if q == 1:
                                cod = input('Digite o código do da bicicleta: ')
                                if cod in bicicletas:
                                    print('--------------------')
                                    print('Codigo: ', cod)
                                    print('Marca: ', bicicletas[cod][0])
                                    print('Modelo: ', bicicletas[cod][1])
                                    print('Valor: ', bicicletas[cod][2])
                                    print('Quantidade: ', bicicletas[cod][3])
                                    print('---------------------')
                                    desejada = int(input('Quantas unidades você deseja: '))
                                    if desejada <= bicicletas[cod][3]:
                                        total = bicicletas[cod][2] * desejada
                                        print(f"O VALOR TOTAL FICARÁ DE R$ {total}")
                                        print('''
#################################
### QUAL A FORMA DE PAGAMENTO ###
### 1 - PIX (10% OFF)         ###
### 2 - ESPÉCIE (5% OFF)      ###
### 3 - CARTÃO                ###
                                            ''')
                                        
                                        pg = int(input('Qual opção você deseja: '))
                                        if pg == 1:
                                            print(f'O total ficou de R${total-((total*10)/100)}')
                                            print('### VENDA FINALIZADA ###')
                                            bicicletas[cod][3]-= desejada
                                            cod_venda= input('Digite o código da venda: ')
                                            vendas[cod_venda]=[clientes[cod_cliente][0], cod_cliente, 'BICICLETA', cod, total, 'PIX', data_hora, 'ATIVA']
                                        elif pg == 2:
                                            print(f'O total ficou de R${total-((total*5)/100)}')
                                            print('### VENDA FINALIZADA ###')
                                            bicicletas[cod][3]-= desejada
                                            cod_venda= input('Digite o código da venda: ')
                                            vendas[cod_venda]=[clientes[cod_cliente][0], cod_cliente, bicicletas[cod][1], bicicletas[cod], total, 'ESPÉCIE', data_hora, 'ATIVA']
                                        elif pg == 3:
                                            vezes = int(input('Deseja dividir em quantas vezes: '))
                                            print(f'O VALOR FINAL FICOU DE {total} dividio em {vezes}x de R${total/vezes} sem juros')
                                            print('VENDA FINALIZADA')
                                            bicicletas[cod][3]-= desejada
                                            cod_venda= input('Digite o código da venda: ')
                                            vendas[cod_venda]=[clientes[cod_cliente][0], cod_cliente, bicicletas[cod][1], bicicletas[cod][2], total, 'CARTÃO', data_hora, 'ATIVA']

                            elif q == 2:
                                cod = input('Digite o código da sapatilha: ')
                                if cod in sapatilhas:
                                    print('--------------------')
                                    print('Codigo: ', cod)
                                    print('Marca: ', sapatilhas[cod][0])
                                    print('Modelo: ', sapatilhas[cod][1])
                                    print('Valor: ', sapatilhas[cod][2])
                                    print('Quantidade: ', sapatilhas[cod][3])
                                    desejada = int(input('Quantas unidades você deseja: '))
                                    if desejada <= sapatilhas[cod][3]:
                                        total = sapatilhas[cod][2] * desejada
                                        print(f"O VALOR TOTAL FICARÁ DE R$ {total}")
                                        print('''
#################################
### QUAL A FORMA DE PAGAMENTO ###
### 1 - PIX (10% OFF)         ###
### 2 - ESPÉCIE (5% OFF)      ###
### 3 - CARTÃO                ###
                                        ''')

                                        pg = int(input('Qual opção você deseja: '))
                                        if pg == 1:
                                            print(f'O total ficou de R$ {total - ((total * 10) / 100)}')
                                            print('### VENDA FINALIZADA ###')
                                            sapatilhas[cod][3] -= desejada
                                            cod_venda= input('Digite o código da venda: ')
                                            vendas[cod_venda]=[clientes[cod_cliente][0], cod_cliente, sapatilhas[cod][1], sapatilhas[cod][2], total, 'PIX', data_hora, 'ATIVA']
                                        elif pg == 2:
                                            print(f'O total ficou de R$ {total - ((total * 5) / 100)}')
                                            print('### VENDA FINALIZADA ###')
                                            sapatilhas[cod][3] -= desejada
                                            cod_venda= input('Digite o código da venda: ')
                                            vendas[cod_venda]=[clientes[cod_cliente][0], cod_cliente, sapatilhas[cod][1], sapatilhas[cod][2], total, 'ESPÉCIE', data_hora, 'ATIVA']
                                        elif pg == 3:
                                            vezes = int(input('Deseja dividir em quantas vezes: '))
                                            print(f'O VALOR FINAL FICOU DE {total} dividido em {vezes}x de R$ {total/vezes}')
                                            print('VENDA FINALIZADA')
                                            sapatilhas[cod][3] -= desejada
                                            cod_venda= input('Digite o código da venda: ')
                                            vendas[cod_venda]=[clientes[cod_cliente][0], cod_cliente, sapatilhas[cod][1], sapatilhas[cod][2], total, 'CARTÃO', data_hora, 'ATIVA']

                            elif q == 3:
                                cod = input('Digite o código do capacete: ')
                                if cod in capacetes:
                                    print('--------------------')
                                    print('Codigo: ', cod)
                                    print('Marca: ', capacetes[cod][0])
                                    print('Modelo: ', capacetes[cod][1])
                                    print('Valor: ', capacetes[cod][2])
                                    print('Quantidade: ', capacetes[cod][3])
                                    desejada = int(input('Quantas unidades você deseja: '))
                                    if desejada <= capacetes[cod][3]:
                                        total = capacetes[cod][2] * desejada
                                        print(f"O VALOR TOTAL FICARÁ DE R$ {total}")
                                        print('''
#################################
### QUAL A FORMA DE PAGAMENTO ###
### 1 - PIX (10% OFF)         ###
### 2 - ESPÉCIE (5% OFF)      ###
### 3 - CARTÃO                ###
                                        ''')
                                        pg = int(input('Qual opção você deseja: '))
                                        if pg == 1:
                                            print(f'O total ficou de R$ {total - ((total * 10) / 100)}')
                                            print('### VENDA FINALIZADA ###')
                                            capacetes[cod][3] -= desejada
                                            cod_venda= input('Digite o código da venda: ')
                                            vendas[cod_venda] = [clientes[cod_cliente][0], cod_cliente, capacetes[cod][1], capacetes[cod][2], total, 'PIX', data_hora, 'ATIVA']
                                        elif pg == 2:
                                            print(f'O total ficou de R$ {total - ((total * 5) / 100)}')
                                            print('### VENDA FINALIZADA ###')
                                            capacetes[cod][3] -= desejada
                                            cod_venda= input('Digite o código da venda: ')
                                            vendas[cod_venda] = [clientes[cod_cliente][0], cod_cliente, capacetes[cod][1], capacetes[cod][2], total, 'ESPÉCIE', data_hora, 'ATIVA']
                                        elif pg == 3:
                                            vezes = int(input('Deseja dividir em quantas vezes: '))
                                            print(f'O VALOR FINAL FICOU DE {total} dividido em {vezes}x de R$ {total/vezes}')
                                            print('VENDA FINALIZADA')
                                            capacetes[cod][3] -= desejada
                                            vendas[cod_venda] = [clientes[cod_cliente][0], cod_cliente, capacetes[cod][1], capacetes[cod][2], total, 'CARTÃO', data_hora, 'ATIVA']

                            elif q == 4:
                                cod = input('Digite o código da roupa: ')
                                if cod in roupas:
                                    print('--------------------')
                                    print('Codigo: ', cod)
                                    print('Marca: ', roupas[cod][0])
                                    print('Tamanho: ', roupas[cod][1])
                                    print('Valor: ', roupas[cod][2])
                                    print('Quantidade: ', roupas[cod][3])
                                    desejada = int(input('Quantas unidades você deseja: '))
                                    if desejada <= roupas[cod][3]:
                                        total = roupas[cod][2] * desejada
                                        print(f"O VALOR TOTAL FICARÁ DE R$ {total}")
                                        print('''
#################################
### QUAL A FORMA DE PAGAMENTO ###
### 1 - PIX (10% OFF)         ###
### 2 - ESPÉCIE (5% OFF)      ###
### 3 - CARTÃO                ###
                                        ''')

                                        pg = int(input('Qual opção você deseja: '))
                                        if pg == 1:
                                            print(f'O total ficou de R$ {total - ((total * 10) / 100)}')
                                            print('### VENDA FINALIZADA ###')
                                            roupas[cod][3] -= desejada
                                            vendas[cod_venda] = [clientes[cod_cliente][0], cod_cliente, roupas[cod][1], roupas[cod][2], total, 'PIX', data_hora, 'ATIVA']
                                        elif pg == 2:
                                            print(f'O total ficou de R$ {total - ((total * 5) / 100)}')
                                            print('### VENDA FINALIZADA ###')
                                            roupas[cod][3] -= desejada
                                            vendas[cod_venda] = [clientes[cod_cliente][0], cod_cliente, roupas[cod][1], roupas[cod][2], total, 'ESPÉCIE', data_hora, 'ATIVA']
                                        elif pg == 3:
                                            vezes = int(input('Deseja dividir em quantas vezes: '))
                                            print(f'O VALOR FINAL FICOU DE {total} dividido em {vezes}x de R$ {total/vezes}')
                                            print('VENDA FINALIZADA')            
                                            roupas[cod][3] -= desejada  
                                            vendas[cod_venda] = [clientes[cod_cliente][0], cod_cliente, roupas[cod][1], roupas[cod][2], total, 'CARTÃO', data_hora, 'ATIVA']
                    elif q == 2:
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
                            print('------------------------') 
                elif q == 3:
                    print('''
##############################
#######   BUSCAR VENDA  ######
##############################
                           ''')
                    cod = input('DIGITE O CÓDIGO DA VENDA QUE VOCÊ DESEJA CONSULTAR: ') 
                    if cod in vendas:
                        print('LISTANDO VENDA....')
                        time.sleep(1)
                        print('------------------------')
                        print('Código da Venda:', cod_venda)
                        print('Cliente:', vendas[cod_venda][0])
                        print('Código Cliente:', vendas[cod_venda][1])
                        print('Produto:', vendas[cod_venda][2])
                        print('Valor: R$', vendas[cod_venda][3])
                        print('Pagamento:', vendas[cod_venda][4])
                        print('Data/Hora:', vendas[cod_venda][5])
                        print('Status:', vendas[cod_venda][6])
                        print('------------------------')      
                elif q == 4:
                    print('######## CANCELAR VENDA #########')
                    cod = input('Digite o código da venda que você deseja cancelar: ')
                    if cod in vendas:
                        print('CANCELANDO VENDA')
                        time.sleep(1)
                        print('VENDA CANCELADA')
                        vendas[cod][6] = 'CANCELADA'
                    else:
                        print('VENDA NÃO ESTÁ NO NOSSO HISTÓRICO')
                     
        elif resp == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''
###################################################
############ 1 - TOTAL FATURADOO           ########
############ 2 - PRODUTO MAIS VENDIDO      ########      
############ 3 - CLIENTES QUE MAIS COMPRAM ########     
############ 4 - QUANTIDADE DE VENDAS      ########
############ 5 - VOLTAR                    ########
                ''')
            q = int(input('Qual opção você deseja: '))

        elif resp == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('''
###################################################
##########      MÓDULO INFORMAÇÕES       ##########
###################################################              
                ''')
            print('''
### PROJETO DA DISCIPLINA DCT1101                                  ###
### TEMA: SISTEMA DE GERENCIAMENTO DE UMA LOJA DE BICICLETA        ###
### DOCENTE RESPONSÁVEL: FLAVIUS GORGÔNIO                          ###
### DISCENTE: JOSÉ EMANUEL DA CÂMARA SILVA                         ### 
### GITHUB: https://github.com/joseemanuelcsilva-spec/Projetos.git ###
                ''')
        elif resp == 0:
            print('''
##### PROGRAMA ENCERRADO ##
                ''')
        else:
            print('OPÇÃO INVÁLIDA')

salvar_bicicletas(bicicletas)
salvar_capacetes(capacetes)
salvar_sapatilhas(sapatilhas)
salvar_roupas(roupas)
salvar_clientes(clientes)
salvar_vendas(vendas)

