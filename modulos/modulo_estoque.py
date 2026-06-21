def menu_estoque():
        resp = ' '
        if resp == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
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
                                    print(bicicletas[cod][0])
                                    print(bicicletas[cod][1])
                                    print(bicicletas[cod][2])
                                    print(bicicletas[cod][3])
                                    print(bicicletas[cod][4])
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
                        os.system('cls' if os.name == 'nt' else 'clear')
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

