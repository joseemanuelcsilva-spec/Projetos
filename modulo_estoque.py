import os
def menu_estoque(bicicletas, capacetes, sapatilhas, roupas):
    q = ''
    while q != 6:
        print('''
###############################################
#         GERENCIAMENTO DE ESTOQUE            #
###############################################
############ 1 - CADASTRAR PRODUTO     ########
############ 2 - LISTAR PRODUTOS       ########      
############ 3 - ATUALIZAR PRODUTO     ########     
############ 4 - BUSCAR PRODUTO        ########
############ 5 - DESATIVAR PRODUTO     ########
############ 6 - VOLTAR                ########            
            ''')
        q = int(input('Qual opção você deseja: '))

        if q == 1:
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
                    status = 'ATIVO'
                    bicicletas[cod] = [marca, modelo, valor, quant, status]
                    print('Produto cadastrado com sucesso!')

                elif q == 2:
                    marca= input('Digite a marca da capacete: ')
                    modelo = input('Digite o modelo da capacete: ')
                    valor = float(input('Digite o valor da capacete: '))
                    cod = str(input('Digite o código da capacete: '))
                    quant = int(input('Quantas unidades:  '))
                    status = 'ATIVO'
                    capacetes[cod] = [marca, modelo, valor, quant, status]
                    print('Produto cadastrado com sucesso!')
                
                elif q == 3:
                    marca = input('Digite a marca da sapatilha: ')
                    modelo = input('Digite o modelo da sapatilha: ')
                    valor= float(input('Digite o valor da sapatilha: '))
                    cod= str(input('Digite o código da sapatilha: '))
                    quant = int(input('Quantas unidades: '))
                    status = 'ATIVO'
                    sapatilhas[cod] = [marca, modelo, valor, quant, status]
                    print('Produto cadastrado com sucesso!')

                elif q == 4:
                    marca = input('Digite a marca da roupa: ')
                    valor= float(input('Digite o valor da roupa: '))
                    tam = input('Digite o tamanho da roupa: ').upper()
                    cod = input('Digite o código da roupa: ')
                    quant = int(input('Quantas unidades:  '))
                    status = 'ATIVO'
                    roupas[cod] = [marca, tam, valor, quant, status]
                    print('Produto cadastrado com sucesso!')
        
        elif q == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
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
                        print('Status', bicicletas[codigo][4])
                        print('--------------------')
                elif q == 2:
                    for codigo in capacetes:
                        print('--------------------')
                        print('Marca:', capacetes[codigo][0])
                        print('Modelo:', capacetes[codigo][1])
                        print('Valor:', capacetes[codigo][2])
                        print('Quantidade:', capacetes[codigo][3])
                        print('Status', capacetes[codigo][4])
                        print('--------------------')
                elif q == 3:
                    for codigo in sapatilhas:
                        print('--------------------')
                        print('Marca:', sapatilhas[codigo][0])
                        print('Modelo:',sapatilhas[codigo][1])
                        print('Valor:', sapatilhas[codigo][2])
                        print('Quantidade:', sapatilhas[codigo][3])
                        print('Status', sapatilhas[codigo][4])
                        print('--------------------')
                elif q == 4:
                    for codigo in roupas:
                        print('--------------------')
                        print('Marca:', roupas[codigo][0])
                        print('Tamanho:', roupas[codigo][1])
                        print('Valor:', roupas[codigo][2])
                        print('Quantidade:', roupas[codigo][3])
                        print('Status', roupas[codigo][4])
                        print('--------------------')
                        
        elif q == 3:
            os.system('cls' if os.name == 'nt' else 'clear')
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
                        print('Codigo:', codigo)
                        print('Marca:', bicicletas[codigo][0])
                        print('Modelo:',bicicletas[codigo][1])
                        print('Valor:',bicicletas[codigo][2])
                        print('Quantidade:',bicicletas[codigo][3])
                    else:
                        print('Bicicleta não encontrada')
                        
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
                            os.system('cls' if os.name == 'nt' else 'clear')
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
                        print('Código:', cod)
                        print('Marca:',capacetes[codigo][0])
                        print('Modelo:', capacetes[codigo][1])
                        print('Valor:', capacetes[codigo][2])
                        print('Quantidade:', capacetes[codigo][3])
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
                        q = int(input('QUAL OPÇÃO VOCÊ DESEJA: '))
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
                            nova_quant = int(input('Digite a nova quantidade: '))
                            capacetes[codigo][3] = nova_quant
                        elif q == 5:
                            novo_cod= input('Digite o novo código do produto: ')
                            capacetes[novo_cod] = capacetes[codigo]
                            del capacetes[codigo]
                            codigo = novo_cod

                elif q == 3:
                    codigo = input('Digite o código da sapatilha: ')
                    if codigo in sapatilhas:
                        print('### SAPATILHA ENCONTRADA ###')
                        print('-----------------------')
                        print('Codigo:', cod)
                        print('Marca:',sapatilhas[codigo][0])
                        print('Modelo:',sapatilhas[codigo][1])
                        print('Valor:',sapatilhas[codigo][2])
                        print('Quantidade:',sapatilhas[codigo][3])
                    else:
                        print('SAPATILHA NÃO ENCONTRADA')

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
                            nova_quant = int(input('Digite a nova quantidade: '))
                            sapatilhas[codigo][3] = nova_quant
                        elif q == 5:
                            novo_cod= input('Digite o novo código do produto: ')
                            sapatilhas[novo_cod] = sapatilhas[codigo]
                            del sapatilhas[codigo]
                            codigo = novo_cod

                elif q == 4:
                    codigo = input('Digite o código da roupa: ')
                    if codigo in roupas:
                        print('### ROUPA ENCONTRADA ###')
                        print('-----------------------')
                        print(roupas[codigo][0])
                        print(roupas[codigo][1])
                        print(roupas[codigo][2])
                        print(roupas[codigo][3])
                    else:
                        print('ROUPA NÃO ENCONTRADA')

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
                            nova_quant = int(input('Digite a nova quantidade: '))
                            roupas[codigo][3] = nova_quant
                        elif q == 5:
                            novo_cod= input('Digite o novo código do produto: ')
                            roupas[novo_cod] = roupas[codigo]
                            del roupas[codigo]
                            codigo = novo_cod
                                                                    
        elif q == 4:
            os.system('cls' if os.name == 'nt' else 'clear')
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
                        print('Codigo', cod)
                        print('Marca:', bicicletas[cod][0])
                        print('Modelo', bicicletas[cod][1])
                        print('Valor: R$',bicicletas[cod][2])
                        print('Quantidade', bicicletas[cod][3])
                        print('Status:', bicicletas[cod][4])
                    else:
                        print('### BICICLETA NÃO ENCONTRADA ###')
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
                        print('Status:', capacetes[cod][4])
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
                        print('Status:', sapatilhas[cod][4])
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
                        print('Status:', roupas[cod][4])
                    else:
                        print('### ROUPA NÃO ENCONTRADA ###')
                            
        elif q == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            q = ' ' 
            while q != 5:
                print('''
###################################################
## DESEJA DESATIVAR PRODUTO DE QUAL CATEGORIA ? ###
###################################################
## 1 - BICICLETAS                               ###
## 2 - CAPACETES                                ###
## 3 - SAPATILHAS                               ###
## 4 - ROUPAS                                   ### 
## 5 - SAIR                                     ###
                ''')
                q = int(input('Qual opção você deseja: '))
                if q == 1:
                    cod = input('Digite o código da bicicleta que você quer remover do estoque: ')
                    if cod in bicicletas:
                        bicicletas[cod][4]= 'DESATIVADA'
                        print('Bicicleta desativada!')
                elif q == 2:
                    cod = input('Digite o código do capacete que você quer remover do estoque: ')  
                    if cod in capacetes:
                        capacetes[cod][4] = 'DESATIVADO'                       
                        print('Capacete desativada!')
                elif q == 3:
                    cod = input('Digite o código da sapatilha que você quer remover do estoque: ')
                    if cod in sapatilhas:
                        sapatilhas[cod][4] = 'DESATIVADO'
                        print('Sapatilha desativada!')
                elif q == 4: 
                    cod = input('Digite o código da roupa que você deseja remover: ')
                    if cod in roupas:
                        roupas[cod][4]= 'DESATIVADO'
                        print('Roupa desativada!')
            else:
                print('Opção invalida')
    
    return bicicletas, capacetes, sapatilhas, roupas