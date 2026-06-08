resp = ' '
estoque = []
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
                        cat = 'Bicicleta'
                        produto = {
        'codigo': cod,
        'categoria': cat,
        'marca': marca,
        'modelo': modelo,
        'valor': valor,
        'quantidade': quant
    }
                        estoque.append(produto) 
                        print('Produto cadastrado com sucesso!')
    
                    elif q == 2:
                        marca= input('Digite a marca da capacete: ')
                        modelo = input('Digite o modelo da capacete: ')
                        valor = float(input('Digite o valor da capacete: '))
                        cod = str(input('Digite o código da capacete: '))
                        quant = int(input('Quantas unidades:  '))
                        cat = 'Capacete'
                        produto = {
        'codigo': cod,
        'categoria': cat,
        'marca': marca,
        'modelo': modelo,
        'valor': valor,
        'quantidade': quant
    }
                        estoque.append(produto) 
                        print('Produto cadastrado com sucesso!')
                    
                    elif q == 3:
                        marca = input('Digite a marca da sapatilha: ')
                        modelo = input('Digite o modelo da sapatilha: ')
                        valor= float(input('Digite o valor da sapatilha: '))
                        cod= str(input('Digite o código da sapatilha: '))
                        cat ='Sapatilha'
                        quant = int(input('Quantas unidades:  '))
                        produto = {
        'codigo': cod,
        'categoria': cat,
        'marca': marca,
        'modelo': modelo,
        'valor': valor,
        'quantidade': quant
    }
                        estoque.append(produto) 
                        print('Produto cadastrado com sucesso!')
                    elif q == 4:
                        marca = input('Digite a marca da roupa: ')
                        valor= float(input('Digite o valor da roupa: '))
                        tam = input('Digite o tamanho da roupa: ').upper()
                        cod = input('Digite o código da roupa: ')
                        quant = int(input('Quantas unidades:  '))
                        cat = 'Roupa'
                        produto = {
        'codigo': cod,
        'categoria': cat,
        'marca': marca,
        'tamanho': tam,
        'valor': valor,
        'quantidade': quant
    }
                        estoque.append(produto) 
                        print('Produto cadastrado com sucesso!')
   
            elif q == 2:
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
                        print('LISTANDO TODAS AS BICICLETAS DO ESTOQUE.....')
                        for produto in estoque:
                            if produto['categoria'] == 'Bicicleta':
                                print('--------------------')
                                print('Código:', produto['codigo'])
                                print('Categoria:', produto['categoria'])
                                print('Marca:', produto['marca'])
                                print('Modelo:', produto['modelo'])
                                print('Valor: R$', produto['valor'])
                                print('Quantidade:', produto['quantidade'])

                    elif q == 2:
                        print('LISTANDO TODOS OS CAPACETES DO ESTOQUE.....')
                        for produto in estoque:
                            if produto['categoria'] == 'Capacete':
                                print('--------------------')
                                print('Código:', produto['codigo'])
                                print('Categoria:', produto['categoria'])
                                print('Marca:', produto['marca'])
                                print('Modelo:', produto['modelo'])
                                print('Valor: R$', produto['valor'])
                                print('Quantidade:', produto['quantidade'])

                    elif q == 3:
                        print('LISTANDO TODAS AS SAPATILHAS DO ESTOQUE.....')
                        for produto in estoque:
                            if produto['categoria'] == 'Sapatilha':
                                print('--------------------')
                                print('Código:', produto['codigo'])
                                print('Categoria:', produto['categoria'])
                                print('Marca:', produto['marca'])
                                print('Modelo:', produto['modelo'])
                                print('Valor: R$', produto['valor'])
                                print('Quantidade:', produto['quantidade'])
                        
                    elif q == 4:
                        print('LISTANDO TODAS AS ROUPAS DO ESTOQUE.....')
                        for produto in estoque:
                            if produto['categoria'] == 'Roupa':
                                print('--------------------')
                                print('Código:', produto['codigo'])
                                print('Categoria:', produto['categoria'])
                                print('Marca:', produto['marca'])
                                print('Tamanho:', produto['tamanho'])
                                print('Valor: R$', produto['valor'])
                                print('Quantidade:', produto['quantidade'])
                       
            elif q == 3:
                cod = input('Digite o código do produto: ')
                for produto in estoque:
                    if produto['codigo'] == cod:
                        print('Produto Encontrado')
                        print('--------------------')
                        print('Código:', produto['codigo'])
                        print('Categoria:', produto['categoria'])
                        print('Marca:', produto['marca'])
                        print('Modelo:', produto['modelo'])
                        print('Valor: R$', produto['valor'])
                        print('Quantidade:', produto['quantidade'])

                    q = ' '
                    while q != 6:
                        print('''
#####################################                              
###### O QUE DESEJA ALTERAR ?? ######
########## 1 - Marca           ######
########## 2 - Modelo          ######
########## 3 - Preço           ######
########## 4 - Quantidade      ######
########## 5 - Código          ######
########## 6 - Voltar          ######
                              ''')
                        q = int(input('Qual opção você deseja: '))
                        if q == 1:
                            produto['marca'] = input('Digite a nova marca: ') 
                        elif q == 2:
                            produto['modelo'] = input('Digite o novo modelo: ')
                        elif q == 3:
                            produto['preco'] = float(input('Digite o novo preço desejado R$: '))
                        elif q == 4:
                            produto['quantidade'] = int(input('Digite a nova quantidade itens desse produto: '))
                        elif q == 5:
                            produto['codigo'] = str(input('Digite o novo código'))

            elif q == 4:
                print('##### VOCÊ ENTROU NO MODO DE PESQUISA ####### ')
                cod = input('Digite o código do produto: ')
                for produto in estoque:
                    if produto['codigo'] == cod:
                        print('Produto Encontrado')
                        print('--------------------')
                        print('Código:', produto['codigo'])
                        print('Categoria:', produto['categoria'])
                        print('Marca:', produto['marca'])
                        print('Modelo:', produto['modelo'])
                        print('Valor: R$', produto['valor'])
                        print('Quantidade:', produto['quantidade'])
                    else:
                        print('### PRODUTO NÃO ENCONTRADO ###')

            elif q == 5:
                remover = str(input('Digite o código do produto que você deseja deletar: '))
                for produto in estoque:
                    if produto['codigo'] == remover:
                        print('### PRODUTO ENCONTRADO ###')
                        certeza = input('TEM CERTEZA QUE DESEJA DELETAR [S/N]:').upper()
                        if certeza == 'S':
                            print('DELETANDO PRODUTO')
                            estoque.remove(produto)
                        
    elif resp == 2:
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

    elif resp == 3:
        print('''
###############################################
############ 1 - NOVA VENDA            ########
############ 2 - HISTÓRICO DE VENDAS   ########      
############ 3 - BUSCAR VENDAS         ########     
############ 4 - VOLTAR                ########       
              ''')
        q = int(input('Qual opção você deseja: '))
    
    elif resp == 4:
        print('''
###################################################
############ 1 - TOTAL FATURADO            ########
############ 2 - PRODUTO MAIS VENDIDO      ########      
############ 3 - CLIENTES QUE MAIS COMPRAM ########     
############ 4 - QUANTIDADE DE VENDAS      ########
############ 5 - VOLTAR                    ########
              ''')
        q = int(input('Qual opção você deseja: '))

    elif resp == 5:
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
##### PROGRAMA ENCERRADO #####
              ''')
    else:
        print('OPÇÃO INVÁLIDA')
    
for produto in estoque:
    print('--------------------')
    print('Código:', produto['codigo'])
    print('Categoria:' )
    print('Marca:', produto['marca'])
    print('Modelo:', produto['modelo'])
    print('Valor:', produto['valor'])
    print('Quantidade:', produto['quantidade'])
