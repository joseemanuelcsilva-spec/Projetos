import os
from datetime import datetime
import time
resp = ' '
# Dicionários 
bicicletas = {
     'b001':['caloi', 'adv', 200, 10]
}
capacetes = {
     'c001':['assasa','sasasa', 90, 10]
}
sapatilhas = {
     's001':['pe de pano', 'asaasa', 9, 3]
}
roupas = {
     'r001':['specialized', 'GG', 10, 4]
}
clientes = {}
vendas = {}

while resp != 0:
        os.system("clear")
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
            os.system("clear")
            q = ' '
            while q != 6:
                print('''
###############################################
#         GERENCIAMENTO DE ESTOQUE            #
###############################################
############ 1 - CADASTRAR PRODUTO     ########
############ 2 - LISTAR PRODUTOS       ########      
############ 3 - ATUALIZAR PRODUTO     ########     
############ 4 - BUSCAR PRODUTO        ########
############ 5 - REMOVER PRODUTO       ########
############ 6 - VOLTAR                ########            
                    ''')
                q = int(input('Qual opção você deseja: '))

                if q == 1:
                    os.system("clear")
                    q = ' '
                    while q != 5: 
                        print('''
################################################
##          PRODUTOS PARA CADASTRAR           ##
################################################                      
######### 1 - BICICLETA              ###########
######### 2 - CAPACETE               ###########
######### 3 - SAPATILHA              ###########
######### 4 - ROUPA DE CICLISMO      ###########
######### 5 - VOLTAR                 ###########
                    ''')
                        q = int(input('Qual opção você deseja: '))
                        if q == 1:
                            marca = input('Digite a marca da Bicicleta: ')
                            modelo = input('Digite o modelo da Bicicleta: ')
                            valor = float(input('Digite o valor da Bicicleta: '))
                            cod = str(input('Digite o código da Bicicleta: '))
                            quant = int(input('Quantas unidades: '))
                            bicicletas[cod] = [marca, modelo, valor, quant]

                            print('Produto cadastrado com sucesso!')
        
                        elif q == 2:
                            marca= input('Digite a marca da capacete: ')
                            modelo = input('Digite o modelo da capacete: ')
                            valor = float(input('Digite o valor da capacete: '))
                            cod = str(input('Digite o código da capacete: '))
                            quant = int(input('Quantas unidades:  '))
                            capacetes[cod] = [marca, modelo, valor, quant]

                            print('Produto cadastrado com sucesso!')
                        
                        elif q == 3:
                            marca = input('Digite a marca da sapatilha: ')
                            modelo = input('Digite o modelo da sapatilha: ')
                            valor= float(input('Digite o valor da sapatilha: '))
                            cod= str(input('Digite o código da sapatilha: '))
                            quant = int(input('Quantas unidades:  '))
                            sapatilhas[cod] = [marca, modelo, valor, quant]

                            print('Produto cadastrado com sucesso!')
                        elif q == 4:
                            marca = input('Digite a marca da roupa: ')
                            valor= float(input('Digite o valor da roupa: '))
                            tam = input('Digite o tamanho da roupa: ').upper()
                            cod = input('Digite o código da roupa: ')
                            quant = int(input('Quantas unidades:  '))
                            roupas[cod] = [marca, tam, valor, quant]

                            print('Produto cadastrado com sucesso!')
    
                elif q == 2:
                    os.system("clear")
                    q = ' '
                    while q != 5:
                        print('''
################################################                      
#####   QUAL ESTOQUE VOCÊ QUER LISTAR      #####
################################################                      
######### 1 - BICICLETA              ###########
######### 2 - CAPACETE               ###########
######### 3 - SAPATILHA              ###########
######### 4 - ROUPA DE CICLISMO      ###########
######### 5 - VOLTAR                 ###########
                        ''')
                        q = int(input('Qual opção você deseja: '))
                        if q == 1:
                            for codigo in bicicletas:
                                print('--------------------')
                                print('Marca:', bicicletas[codigo][0])
                                print('Modelo:', bicicletas[codigo][1])
                                print('Valor:', bicicletas[codigo][2])
                                print('Quantidade:', bicicletas[codigo][3])
                                print('--------------------')
                        elif q == 2:
                            for codigo in capacetes:
                                print('--------------------')
                                print('Marca:', capacetes[codigo][0])
                                print('Modelo:', capacetes[codigo][1])
                                print('Valor:', capacetes[codigo][2])
                                print('Quantidade:', capacetes[codigo][3])
                                print('--------------------')
                        elif q == 3:
                            for codigo in sapatilhas:
                                print('--------------------')
                                print('Marca:', sapatilhas[codigo][0])
                                print('Modelo:',sapatilhas[codigo][1])
                                print('Valor:', sapatilhas[codigo][2])
                                print('Quantidade:', sapatilhas[codigo][3])
                                print('--------------------')
                        elif q == 4:
                            for codigo in roupas:
                                print('--------------------')
                                print('Marca:', roupas[codigo][0])
                                print('Tamanho:', roupas[codigo][1])
                                print('Valor:', roupas[codigo][2])
                                print('Quantidade:', roupas[codigo][3])
                                print('--------------------')
                elif q == 3:
                    os.system("clear")
                    q = ' '
                    while q != 5:
                        print('''
###############################
###### ATUALIZAR PRODUTO ######
###############################
### 1 - BICICLETAS       ######
### 2 - CAPACETES        ######
### 3 - SAPATILHAS       ######
### 4 - ROUPAS           ###### 
### 5 - SAIR             ######
                            
                                ''')
                        q = int(input('Qual opção você deseja:'))
                        if q == 1:
                                codigo = input('Digite o código da bicicleta que você deseja alterar as informações:')
                                if codigo in bicicletas:
                                    print('### Bicicleta encontrada ###')
                                    print('-----------------------')
                                    print(bicicletas[codigo])
                                    print(bicicletas[codigo][0])
                                    print(bicicletas[codigo][1])
                                    print(bicicletas[codigo][2])
                                    print(bicicletas[codigo][3])
                                else:
                                    print('Bicicleta não encotrada')
                                while q != 6:
                                        print('''
##############################                                  
### O QUE DESEJA ALTERAR ? ###
##############################
### 1 - MARCA              ###
### 2 - MODELO             ###
### 3 - VALOR              ###
### 4 - QUANTIDADE         ###
### 5 - CÓDIGO             ###
### 6 - VOLTAR             ###
##############################
                                        ''')
                                        q = int(input('QUAL OPÇÃO VOCÊ DESEJA: '))
                                        if q == 1:
                                            os.system("clear")
                                            nova_marca = input('Digite a nova marca da bicicleta: ')
                                            bicicletas[codigo][0] = nova_marca
                                            
                                        elif q == 2:
                                            novo_modelo = input('Digite o novo modelo da bicicleta: ')
                                            bicicletas[codigo][1] = novo_modelo
                                           
                                        elif q == 3:
                                            novo_valor = float(input('Digite o novo valor: R$ '))
                                            bicicletas[codigo][2] = novo_valor
                                            
                                        elif q == 4:
                                            nova_quant = int(input('Digite a nova quantidade no estoque: '))
                                            bicicletas[codigo][3] = nova_quant
                                            
                                        elif q == 5:
                                            novo_cod = input('Novo código: ')
                                            bicicletas[novo_cod] = bicicletas[codigo]
                                            del bicicletas[codigo]
                                            codigo = novo_cod
                                            
                        elif q == 2:
                                        codigo = input('Digite o código do capacete: ')
                                        if codigo in capacetes:
                                            print('### CAPACETE ENCONTRADO ###')
                                            print('-----------------------')
                                            print(capacetes[codigo][0])
                                            print(capacetes[codigo][1])
                                            print(capacetes[codigo][2])
                                            print(capacetes[codigo][3])
                                        else:
                                            print('CAPACETE NÃO ENCONTRADO')

                                        while q != 6:
                                            print('''
##############################                                  
### O QUE DESEJA ALTERAR ? ###
##############################
### 1 - MARCA              ###
### 2 - MODELO             ###
### 3 - VALOR              ###
### 4 - QUANTIDADE         ###
### 5 - CÓDIGO             ###
### 6 - VOLTAR             ###
##############################
                                                ''')
                                            if q == 1:
                                                nova_marca = input('Digite a nova marca do produto:')
                                                capacetes[codigo][0] = nova_marca
                                                
                                            elif q == 2:
                                                novo_modelo = input('Digite o novo modelo desejado: ')
                                                capacetes[codigo][1] = novo_modelo
                                               
                                            elif q == 3:
                                                novo_valor = float(input('Digite o novo valor: '))
                                                capacetes[codigo][2] = novo_valor
                                               
                                            elif q == 4:
                                                nova_quant = int(input('Digite o novo preço deseja: '))
                                                capacetes[codigo][3] = nova_quant
                                                
                                            elif q == 5:
                                                novo_cod= input('Digite o novo códgio do produto: ')
                                                capacetes[novo_cod] = capacetes[codigo]
                                                del capacetes[codigo]
                                                cod = novo_cod
                                                

                        elif q == 3:
                                        codigo = input('Digite o código da sapatilha: ')

                                        if codigo in sapatilhas:
                                            print('### CAPACETE ENCONTRADO ###')
                                            print('-----------------------')
                                            print(sapatilhas[codigo][0])
                                            print(sapatilhas[codigo][1])
                                            print(sapatilhas[codigo][2])
                                            print(sapatilhas[codigo][3])
                                        else:
                                            print('SAPATILHA NÃO ENCONTRADO')

                                        while q != 6:
                                            print('''
    ##############################                                  
    ### O QUE DESEJA ALTERAR ? ###
    ##############################
    ### 1 - MARCA              ###
    ### 2 - MODELO             ###
    ### 3 - VALOR              ###
    ### 4 - QUANTIDADE         ###
    ### 5 - CÓDIGO             ###
    ### 6 - VOLTAR             ###
    ##############################
                                                ''')
                                            q = int(input('Digite a opção que vc deseja: '))


                                            if q == 1:
                                                nova_marca = input('Digite a nova marca do produto:')
                                                sapatilhas[codigo][0] = nova_marca
                                                

                                            elif q == 2:
                                                novo_modelo = input('Digite o novo modelo desejado: ')
                                                sapatilhas[codigo][1] = novo_modelo
                                                
                                            elif q == 3:
                                                novo_valor = float(input('Digite o novo valor: '))
                                                sapatilhas[codigo][2] = novo_valor
                                                
                                            elif q == 4:
                                                nova_quant = int(input('Digite o novo preço deseja: '))
                                                sapatilhas[codigo][3] = nova_quant

                                            elif q == 5:
                                                novo_cod= input('Digite o novo códgio do produto: ')
                                                sapatilhas[novo_cod] = sapatilhas[codigo]
                                                del sapatilhas[codigo]
                                                cod = novo_cod
                                                

                        elif q == 4:
                                    codigo = input('Digite o código da roupa: ')

                                    if codigo in sapatilhas:
                                            print('### CAPACETE ENCONTRADO ###')
                                            print('-----------------------')
                                            print(sapatilhas[codigo][0])
                                            print(sapatilhas[codigo][1])
                                            print(sapatilhas[codigo][2])
                                            print(sapatilhas[codigo][3])
                                    else:
                                            print('SAPATILHA NÃO ENCONTRADO')

                                    while q != 6:
                                            print('''
##############################                                  
### O QUE DESEJA ALTERAR ? ###
##############################
### 1 - MARCA              ###
### 2 - MODELO             ###
### 3 - VALOR              ###
### 4 - QUANTIDADE         ###
### 5 - CÓDIGO             ###
### 6 - VOLTAR             ###
##############################
                                                ''')
                                            q = int(input('Digite a opção que vc deseja: '))    
                                            if q == 1:
                                                nova_marca = input('Digite a nova marca do produto:')
                                                roupas[codigo][0] = nova_marca
                                               
                                            elif q == 2:
                                                novo_tamanho = input('Digite o tamanho: ').upper()
                                                roupas[codigo][1] = novo_tamanho
                                                

                                            elif q == 3:
                                                novo_valor = float(input('Digite o novo valor : '))
                                                roupas[codigo][2] = novo_valor
                                               

                                            elif q == 4:
                                                nova_quant = int(input('Digite o novo preço deseja: '))
                                                roupas[codigo][3] = nova_quant
                                                
                                            elif q == 5:
                                                novo_cod= input('Digite o novo códgio do produto: ')
                                                roupas[novo_cod] = roupas[codigo]
                                                del roupas[codigo]
                                                cod = novo_cod
                                                                
                elif q == 4:
                    os.system('clear')
                    q = ' '
                    while q != 5:
                        print('''
##############################
##### CONSULTAR ESTOQUE  #####
##############################
### 1 - BICICLETAS      ######
### 2 - CAPACETES       ######
### 3 - SAPATILHAS      ######
### 4 - ROUPAS          ###### 
### 5 - SAIR            ######
                          ''')
                        q = int(input('QUAL ESTOQUE VOCÊ QUER CONSULTAR ?'))
                        if q == 1:
                            cod = input('Digite o código da bicicleta: ')
                            if cod in bicicletas:
                                print('### BICICLETA ENCONTRADA ###')
                                print('-------------------------------')
                                print(bicicletas[cod][0])
                                print(bicicletas[cod][1])
                                print(bicicletas[cod][2])
                                print(bicicletas[cod][3])
                                print(bicicletas[cod][4])
                            else:
                                 print('### BICICLETA NÃO ENCONTRADA')
                        elif q == 2:
                            cod = input('Digite o código do capacete: ')
                            if cod in capacetes:
                                print('### CAPACETE ENCONTRADO ###')
                                print('-------------------------------')
                                print('Código:', cod)
                                print('Marca:', capacetes[cod][0])
                                print('Modelo:', capacetes[cod][1])
                                print('Valor: R$', capacetes[cod][2])
                                print('Quantidade:', capacetes[cod][3])
                            else:
                                print('### CAPACETE NÃO ENCONTRADO ###')
                        elif q == 3:
                            cod = input('Digite o código da sapatilha: ')
                            if cod in sapatilhas:
                                print('### SAPATILHA ENCONTRADA ###')
                                print('-------------------------------')
                                print('Código:', cod)
                                print('Marca:', sapatilhas[cod][0])
                                print('Modelo:', sapatilhas[cod][1])
                                print('Valor: R$', sapatilhas[cod][2])
                                print('Quantidade:', sapatilhas[cod][3])
                            else:
                                print('### SAPATILHA NÃO ENCONTRADA ###')
                        elif q == 4:
                            cod = input('Digite o código da roupa: ')
                            if cod in roupas:
                                print('### ROUPA ENCONTRADA ###')
                                print('-------------------------------')
                                print('Código:', cod)
                                print('Marca:', roupas[cod][0])
                                print('Tamanho:', roupas[cod][1])
                                print('Valor: R$', roupas[cod][2])
                                print('Quantidade:', roupas[cod][3])
                            else:
                                print('### ROUPA NÃO ENCONTRADA ###')
                        
                elif q == 5:
                    os.system("clear")
                    while q != 5:
                        print('''
#################################################
## DESEJA REMOVER PRODUTO DE QUAL CATEGORIA ? ###
#################################################
## 1 - BICICLETAS                             ###
## 2 - CAPACETES                              ###
## 3 - SAPATILHAS                             ###
## 4 - ROUPAS                                 ### 
## 5 - SAIR                                   ###
                               ''')
                        q = int(input('Qual opção você deseja: '))
                        if q == 1:
                             cod = input('Digite o código da bicicleta que você quer remover do estoque: ')
                             del bicicletas[cod]
                        elif q == 2:
                             cod = input('Digite o código do capacete que você quer remover do estoque: ')  
                             del capacetes[cod]                       
                        elif q == 3:
                             cod = input('Digite o código da sapatilha que você quer remover do estoque: ')
                             del sapatilhas[cod]
                        elif q == 4: 
                             cod = input('DIgite o código da roupa que você deseja remover: ')
                             del roupas[cod]

        elif resp == 2:
            os.system("clear")
            q = ' '
            while q != 6:
                print('''
###############################################
############ 1 - CADASTRAR CLIENTES    ########
############ 2 - LISTAR CLIENTES       ########      
############ 3 - BUSCAR CLIENTES       ########     
############ 4 - ATUALIZAR CADASTRO    ########
############ 5 - REMOVER CADASTRO      ########
############ 6 - VOLTAR                ########            
                ''')
                q = int(input('Qual opção você deseja: '))
                if q == 1:
                    nome = input('Digite o nome do cliente: ')
                    sobrenome = input('Digite o sobrenome do cliente: ')
                    tel = input('Digite o telefone do cliente; xx xxxxx-xxxx ')
                    cpf = input('Digite o cpf do cliente:XXX.XXX.XXX-XX ')
                    cod = input('Digite o código do cliente: ')
                    clientes[cod] = [nome, sobrenome, tel, cpf, cod]
                    print('CLIENTE CADASTRADO COM SUCESSO')
                elif q == 2:
                    print('LISTANDO OS CLIENTES ....')
                    for cod in clientes:
                        print('Codigo:', cod)
                        print('Nome:', clientes[cod][0])
                        print('Sobrenome:', clientes[cod][1])
                        print('Telefone:', clientes[cod][2])
                        print('CPF:', clientes[cod][3])
                        print('-------------------------------------')
                elif q == 3:
                    print('''
##### PESQUISAR CLIENTE #####
                           ''')
                    cod = input('Digite o código do cliente: ')
                    if cod in clientes:
                        print('### CLIENTE ENCONTRADO ###')
                        print(cod) 
                        print('Nome:', clientes[cod][0])
                        print('Sobrenome:',clientes[cod][1])
                        print('Telefone:', clientes[cod][2])
                        print('CPF:', clientes[cod][3])
                    else:
                         print('#### CLIENTE NÃO FOI ENCONTRADO ####')
                elif q == 4:
                    print('''
###############################
#### MÓDULO DE ATUALIZAÇÃO ####
###############################
                           ''')
                    cod = input('Digite o código do cliente: ')
                    if cod in clientes:
                        print(
                             '### CLIENTE ENCONTRADO ###')
                        print(cod) 
                        print('Nome:', clientes[cod][0])
                        print('Sobrenome:',clientes[cod][1])
                        print('Telefone:', clientes[cod][2])
                        print('CPF:', clientes[cod][3])
                        print('')
                        while q != 6:
                            q = ' '
                            print('''
##############################                              
### O QUE DESEJA ALTERAR ? ###
##############################
### 1 - NOME               ###
### 2 - SOBRENOME          ###
### 3 - TELEFONE           ###
### 4 - CPF                ###
### 5 - CÓDIGO             ###
### 6 - VOLTAR             ###
                              ''')
                            q = int(input('Qual opção você deseja: '))
                                
                            if q == 1:
                                        novo_nome = input('DIgite o novo nome: ')
                                        clientes[cod][0] = novo_nome
                            elif q == 2:
                                        novo_sobrenome = input('Digite o novo sobrenome desejado: ')
                                        clientes[cod][1] = novo_sobrenome
                            elif q == 3:
                                        novo_tel = input('DIgite o novo número XX XXXXX-XXX: ')
                                        clientes[cod][2]= novo_tel
                            elif q == 4: 
                                        novo_cpf = input('Digite o novo cpf XXX.XXX.XXX-XX:')
                                        clientes[cod][3] = novo_cpf
                            elif q == 5:
                                        novo_codigo = input('Digite o novo codigo:')
                                        clientes[novo_codigo] = clientes[cod]
                                        del clientes[cod]
                    else:
                        print('CLIENTE NÃO ENCONTRADO')
                    
                elif q == 5:
                    print('''
###########################                          
##### DELETAR CADASTRO ####
###########################                          
                          ''')
                    novo_codigo = input('Digite o novo codigo: ')
                    clientes[novo_codigo] = clientes[cod]
                    clientes[novo_codigo]['código'] = novo_codigo
                    del clientes[cod]
                    cod = novo_codigo
                    print('Código alterado com sucesso!')

# MODULO DE VENDASSSSS

        elif resp == 3:
            os.system("clear")
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
                    os.system('clear')
                    print('#### VAMOS INCIAR UMA VENDA ####')
                    cod_cliente = input('Digite o código do cliente: ')
                    if cod_cliente in clientes: 
                        print('Cliente encontrado')
                        print(f"Seja bem vindo {clientes[cod][0]}")
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
                                            vendas[cod_venda]=[clientes[cod], clientes[cod][0], bicicletas[cod][1], bicicletas[cod][2], total, 'PIX', data_hora, 'ATIVA']
                                        elif pg == 2:
                                            print(f'O total ficou de R${total-((total*5)/100)}')
                                            print('### VENDA FINALIZADA ###')
                                            bicicletas[cod][3]-= desejada
                                            cod_venda= input('Digite o código da venda: ')
                                            vendas[cod_venda]=[clientes[cod], clientes[cod][0], bicicletas[cod][1], bicicletas[cod][2], total, 'ESPÉCIE', data_hora, 'ATIVA']
                                        elif pg == 3:
                                            vezes = int(input('Deseja dividir em quantas vezes: '))
                                            print(f'O VALOR FINAL FICOU DE {total} dividio em {vezes}x de R${total/vezes} sem juros')
                                            print('VENDA FINALIZADA')
                                            bicicletas[cod]['quantidade']-= desejada
                                            cod_venda= input('Digite o código da venda: ')
                                            vendas[cod_venda]=[clientes[cod], clientes[cod][0], bicicletas[cod][1], bicicletas[cod][2], total, 'CARTÃO', data_hora, 'ATIVA']

                                        
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
                                            sapatilhas[cod]['quantidade'] -= desejada
                                            cod_venda= input('Digite o código da venda: ')
                                            vendas[cod_venda]=[clientes[cod], clientes[cod][0], sapatilhas[cod][1], sapatilhas[cod][2], total, 'PIX', data_hora, 'ATIVA']
                                        elif pg == 2:
                                            print(f'O total ficou de R$ {total - ((total * 5) / 100)}')
                                            print('### VENDA FINALIZADA ###')
                                            sapatilhas[cod]['quantidade'] -= desejada
                                            cod_venda= input('Digite o código da venda: ')
                                            vendas[cod_venda]=[clientes[cod], clientes[cod][0], sapatilhas[cod][1], sapatilhas[cod][2], total, 'ESPÉCIE', data_hora, 'ATIVA']
                                        elif pg == 3:
                                            vezes = int(input('Deseja dividir em quantas vezes: '))
                                            print(f'O VALOR FINAL FICOU DE {total} dividido em {vezes}x de R$ {total/vezes}')
                                            print('VENDA FINALIZADA')
                                            sapatilhas[cod]['quantidade'] -= desejada
                                            cod_venda= input('Digite o código da venda: ')
                                            vendas[cod_venda]=[clientes[cod], clientes[cod][0], sapatilhas[cod][1], sapatilhas[cod][2], total, 'CARTÃO', data_hora, 'ATIVA']

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
                                            vendas[cod_venda] = {
                                                'cliente': cod_cliente,
                                                'nome': clientes[cod_cliente][0],
                                                'produto': capacetes[cod][1],
                                                'modelo': capacetes[cod][2],
                                                'valor': total,
                                                'pagamento': 'PIX',
                                                'datahora': data_hora,
                                                'STATUS': 'ATIVA'
                                            }
                                        elif pg == 2:
                                            print(f'O total ficou de R$ {total - ((total * 5) / 100)}')
                                            print('### VENDA FINALIZADA ###')
                                            capacetes[cod]['quantidade'] -= desejada
                                            cod_venda= input('Digite o código da venda: ')
                                            vendas[cod_venda] = {
                                                'cliente': cod_cliente,
                                                'nome': clientes[cod_cliente]['nome'],
                                                'produto': capacetes[cod]['marca'],
                                                'modelo': capacetes[cod]['modelo'],
                                                'valor': total,
                                                'pagamento': 'ESPÉCIE',
                                                'datahora': data_hora,
                                                'STATUS': 'ATIVA'
                                            }
                                        elif pg == 3:
                                            vezes = int(input('Deseja dividir em quantas vezes: '))
                                            print(f'O VALOR FINAL FICOU DE {total} dividido em {vezes}x de R$ {total/vezes}')
                                            print('VENDA FINALIZADA')
                                            capacetes[cod]['quantidade'] -= desejada
                                            vendas[cod_venda] = {
                                                'cliente': cod_cliente,
                                                'nome': clientes[cod_cliente]['nome'],
                                                'produto': capacetes[cod]['marca'],
                                                'modelo': capacetes[cod]['modelo'],
                                                'valor': total,
                                                'pagamento': 'CARTÃO',
                                                'datahora': data_hora,
                                                'STATUS': 'ATIVA'
                                            }

                            elif q == 4:
                                cod = input('Digite o código da roupa: ')
                                if cod in roupas:
                                    print('--------------------')
                                    print('Codigo: ', roupas[cod]['codigo'])
                                    print('Marca: ', roupas[cod]['marca'])
                                    print('Tamanho: ', roupas[cod]['tamanho'])
                                    print('Valor: ', roupas[cod]['valor'])
                                    print('Quantidade: ', roupas[cod]['quantidade'])
                                    desejada = int(input('Quantas unidades você deseja: '))
                                    if desejada <= roupas[cod]['quantidade']:
                                        total = roupas[cod]['valor'] * desejada
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
                                            roupas[cod]['quantidade'] -= desejada
                                            vendas[cod_venda] = {
                                                'cliente': cod_cliente,
                                                'nome': clientes[cod_cliente]['nome'],
                                                'produto': roupas[cod]['marca'],
                                                'tamanho': roupas[cod]['tamanho'],
                                                'valor': total,
                                                'pagamento': 'PIX',
                                                'datahora': data_hora,
                                                'STATUS': 'ATIVA'
                                            }
                                        elif pg == 2:
                                            print(f'O total ficou de R$ {total - ((total * 5) / 100)}')
                                            print('### VENDA FINALIZADA ###')
                                            roupas[cod]['quantidade'] -= desejada
                                            vendas[cod_venda] = {
                                                'cliente': cod_cliente,
                                                'nome': clientes[cod_cliente]['nome'],
                                                'produto': roupas[cod]['marca'],
                                                'tamanho': roupas[cod]['tamanho'],
                                                'valor': total,
                                                'pagamento': 'ESPÉCIE',
                                                'datahora': data_hora,
                                                'STATUS': 'ATIVA'
                                            }
                                        elif pg == 3:
                                            vezes = int(input('Deseja dividir em quantas vezes: '))
                                            print(f'O VALOR FINAL FICOU DE {total} dividido em {vezes}x de R$ {total/vezes}')
                                            print('VENDA FINALIZADA')            
                                            roupas[cod]['quantidade'] -= desejada  
                                            vendas[cod_venda] = {
                                                'cliente': cod_cliente,
                                                'nome': clientes[cod_cliente]['nome'],
                                                'produto': roupas[cod]['marca'],
                                                'tamanho': roupas[cod]['tamanho'],
                                                'valor': total,
                                                'pagamento': 'CARTÃO',
                                                'datahora': data_hora,
                                                'STATUS': 'ATIVA'
                                            }
                elif q == 2:
                    for cod_venda in vendas:
                        print('------------------------')
                        print('Código da Venda:', cod_venda)
                        print('Cliente:', vendas[cod_venda]['nome'])
                        print('Código Cliente:', vendas[cod_venda]['cliente'])
                        print('Produto:', vendas[cod_venda]['produto'])
                        print('Valor: R$', vendas[cod_venda]['valor'])
                        print('Pagamento:', vendas[cod_venda]['pagamento'])
                        print('Data/Hora:', vendas[cod_venda]['datahora'])
                        print('Status:', vendas[cod_venda]['STATUS'])
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
                        print('Cliente:', vendas[cod_venda]['nome'])
                        print('Código Cliente:', vendas[cod_venda]['cliente'])
                        print('Produto:', vendas[cod_venda]['produto'])
                        print('Valor: R$', vendas[cod_venda]['valor'])
                        print('Pagamento:', vendas[cod_venda]['pagamento'])
                        print('Data/Hora:', vendas[cod_venda]['datahora'])
                        print('Status:', vendas[cod_venda]['STATUS'])
                        print('------------------------')      
                elif q == 4:
                    print('######## CANCELAR VENDA #########')
                    cod = input('Digite o código da venda que você deseja cancelar: ')
                    if cod in vendas:
                        print('CANCELANDO VENDA')
                        time.sleep(1)
                        print('VENDA CANCELADA')
                        vendas[cod]['STATUS'] = 'CANCELADA'
                    else:
                        print('VENDA NÃO ESTÁ NO NOSSO HISTÓRICO')
                     
        elif resp == 4:
            os.system("clear")
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
            os.system("clear")
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
##### PROGRAMA ENCERRADO#####
                ''')
        else:
            print('OPÇÃO INVÁLIDA')
print(bicicletas)