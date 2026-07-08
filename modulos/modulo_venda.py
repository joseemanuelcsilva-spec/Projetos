import time
from datetime import datetime
import os
def menu_venda(vendas, bicicletas, capacetes, sapatilhas, roupas, clientes):
   
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
                try:
                    q = int(input('Qual opção você deseja: '))
                except ValueError:
                    print('Entrada inválida! Por favor, escolha um número de 1 a 5.')
                agora = datetime.now()
                data_hora = agora.strftime("%d/%m/%Y %H:%M:%S")

                if q == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('#### VAMOS INCIAR UMA VENDA ####')
                    cod_cliente = input('Digite o código do cliente: ').upper()

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
                            try:
                                q = int(input('Digite a opção desejada: '))
                            except ValueError:
                                print('Entrada inválida! Por favor, escolha um número de 1 a 5.')
                            if q == 1:
                                os.system('cls' if os.name == 'nt' else 'clear')
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
                                        try:
                                            pg = int(input('Qual opção você deseja: '))
                                        except ValueError:
                                            print('Entrada inválida! Por favor, escolha um número de 1 a 3.')
                                        if pg == 1:
                                            print(f'O total ficou de R${total-((total*10)/100)}')
                                            print('### VENDA FINALIZADA ###')
                                            bicicletas[cod][3]-= desejada
                                            cod_venda= input('Digite o código da venda: ').upper()
                                            vendas[cod_venda]=[clientes[cod_cliente][0], cod_cliente, 'BICICLETA', cod, total, 'PIX', data_hora, 'ATIVA']
                                        elif pg == 2:
                                            print(f'O total ficou de R${total-((total*5)/100)}')
                                            print('### VENDA FINALIZADA ###')
                                            bicicletas[cod][3]-= desejada
                                            cod_venda= input('Digite o código da venda: ').upper()
                                            vendas[cod_venda]=[clientes[cod_cliente][0], cod_cliente, 'BICICLETA', cod, total, 'ESPÉCIE', data_hora, 'ATIVA']
                                        elif pg == 3:
                                            vezes = int(input('Deseja dividir em quantas vezes: '))
                                            print(f'O VALOR FINAL FICOU DE {total} dividio em {vezes}x de R${total/vezes} sem juros')
                                            print('VENDA FINALIZADA')
                                            bicicletas[cod][3]-= desejada
                                            cod_venda= input('Digite o código da venda: ').upper()
                                            vendas[cod_venda]=[clientes[cod_cliente][0], cod_cliente, 'BICICLETA', cod, total, 'CARTÃO', data_hora, 'ATIVA']
                                    else:
                                        print('Não temos essa quantidade no estoque!!!')

                            elif q == 2:
                                os.system('cls' if os.name == 'nt' else 'clear')
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
                                        try:
                                            pg = int(input('Qual opção você deseja: '))
                                        except ValueError:
                                            print('Entrada inválida! Por favor, escolha um número de 1 a 3.')
                                        if pg == 1:
                                            print(f'O total ficou de R$ {total - ((total * 10) / 100)}')
                                            print('### VENDA FINALIZADA ###')
                                            sapatilhas[cod][3] -= desejada
                                            cod_venda= input('Digite o código da venda: ').upper()
                                            vendas[cod_venda]=[clientes[cod_cliente][0], cod_cliente, 'SAPATILHA', cod, total, 'PIX', data_hora, 'ATIVA']
                                        elif pg == 2:
                                            print(f'O total ficou de R$ {total - ((total * 5) / 100)}')
                                            print('### VENDA FINALIZADA ###')
                                            sapatilhas[cod][3] -= desejada
                                            cod_venda= input('Digite o código da venda: ').upper()
                                            vendas[cod_venda]=[clientes[cod_cliente][0], cod_cliente, 'SAPATILHA', cod, total, 'ESPÉCIE', data_hora, 'ATIVA']
                                        elif pg == 3:
                                            vezes = int(input('Deseja dividir em quantas vezes: '))
                                            print(f'O VALOR FINAL FICOU DE {total} dividido em {vezes}x de R$ {total/vezes}')
                                            print('VENDA FINALIZADA')
                                            sapatilhas[cod][3] -= desejada
                                            cod_venda= input('Digite o código da venda: ').upper()
                                            vendas[cod_venda]=[clientes[cod_cliente][0], cod_cliente, 'SAPATILHA', cod, total, 'CARTÃO', data_hora, 'ATIVA']
                                    else:
                                        print('Não temos essa quantidade no estoque!!!')

                            elif q == 3:
                                os.system('cls' if os.name == 'nt' else 'clear')
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
                                        try:
                                            pg = int(input('Qual opção você deseja: '))
                                        except ValueError:
                                            print('Entrada inválida! Por favor, escolha um número de 1 a 3.')
                                        if pg == 1:
                                            print(f'O total ficou de R$ {total - ((total * 10) / 100)}')
                                            print('### VENDA FINALIZADA ###')
                                            capacetes[cod][3] -= desejada
                                            cod_venda= input('Digite o código da venda: ').upper()
                                            vendas[cod_venda] = [clientes[cod_cliente][0], cod_cliente, 'CAPACETE', cod, total, 'PIX', data_hora, 'ATIVA']
                                        elif pg == 2:
                                            print(f'O total ficou de R$ {total - ((total * 5) / 100)}')
                                            print('### VENDA FINALIZADA ###')
                                            capacetes[cod][3] -= desejada
                                            cod_venda= input('Digite o código da venda: ').upper()
                                            vendas[cod_venda] = [clientes[cod_cliente][0], cod_cliente, 'CAPACETE', cod, total, 'ESPÉCIE', data_hora, 'ATIVA']
                                        elif pg == 3:
                                            vezes = int(input('Deseja dividir em quantas vezes: '))
                                            print(f'O VALOR FINAL FICOU DE {total} dividido em {vezes}x de R$ {total/vezes}')
                                            print('VENDA FINALIZADA')
                                            capacetes[cod][3] -= desejada
                                            cod_venda= input('Digite o código da venda: ').upper()
                                            vendas[cod_venda] = [clientes[cod_cliente][0], cod_cliente, 'CAPACETE', cod, total, 'CARTÃO', data_hora, 'ATIVA']
                                    else:
                                        print('Não temos essa quantidade no estoque!!!')

                            elif q == 4:
                                os.system('cls' if os.name == 'nt' else 'clear')
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
                                            cod_venda= input('Digite o código da venda: ').upper()
                                            vendas[cod_venda] = [clientes[cod_cliente][0], cod_cliente, 'ROUPAS', cod, total, 'PIX', data_hora, 'ATIVA']
                                        elif pg == 2:
                                            print(f'O total ficou de R$ {total - ((total * 5) / 100)}')
                                            print('### VENDA FINALIZADA ###')
                                            roupas[cod][3] -= desejada
                                            cod_venda= input('Digite o código da venda: ').upper()
                                            vendas[cod_venda] = [clientes[cod_cliente][0], cod_cliente, 'ROUPAS', cod, total, 'ESPÉCIE', data_hora, 'ATIVA']
                                        elif pg == 3:
                                            vezes = int(input('Deseja dividir em quantas vezes: '))
                                            print(f'O VALOR FINAL FICOU DE {total} dividido em {vezes}x de R$ {total/vezes}')
                                            print('VENDA FINALIZADA')            
                                            roupas[cod][3] -= desejada  
                                            cod_venda= input('Digite o código da venda: ').upper()
                                            vendas[cod_venda] =  [clientes[cod_cliente][0], cod_cliente, 'ROUPAS', cod, total, 'CARTÃO', data_hora, 'ATIVA']
                                    else:
                                        print('Não temos essa quantidade no estoque!!!')
                    else:
                        print('cliente não encontrado')

                elif q == 2:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        for cod_venda in vendas:
                            print('-------------------------------------')
                            print('Código da Venda:', cod_venda)
                            print('Cliente:', vendas[cod_venda][0])
                            print('Código Cliente:', vendas[cod_venda][1])
                            print('Produto:', vendas[cod_venda][2])
                            print('Código Produto:', vendas[cod_venda][3])
                            print('Valor: R$', vendas[cod_venda][4])
                            print('Pagamento:', vendas[cod_venda][5])
                            print('Data/Hora:', vendas[cod_venda][6])
                            print('Status:', vendas[cod_venda][7])
                            
                elif q == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('''
##############################
#######   BUSCAR VENDA  ######
##############################
                           ''')
                    cod = input('DIGITE O CÓDIGO DA VENDA QUE VOCÊ DESEJA CONSULTAR: ').upper() 
                    if cod in vendas:
                        print('LISTANDO VENDA....')
                        time.sleep(1)
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
                    else:
                        print('Venda não encontrada')
          
                elif q == 4:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('######## CANCELAR VENDA #########')
                    cod = input('Digite o código da venda que você deseja cancelar: ').upper()
                    if cod in vendas:
                        print('CANCELANDO VENDA')
                        time.sleep(1)
                        print('VENDA CANCELADA')
                        vendas[cod][7] = 'CANCELADA'
                    else:
                        print('VENDA NÃO ESTÁ NO NOSSO HISTÓRICO')
        
    return vendas