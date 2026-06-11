import os
resp = ' '
bicicletas = {}
capacetes = {}
sapatilhas = {}
roupas = {}
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
                        bicicletas[cod] = {
    'marca': marca,
    'modelo': modelo,
    'valor': valor,
    'quantidade': quant
}
                        print('Produto cadastrado com sucesso!')
    
                    elif q == 2:
                        marca= input('Digite a marca da capacete: ')
                        modelo = input('Digite o modelo da capacete: ')
                        valor = float(input('Digite o valor da capacete: '))
                        cod = str(input('Digite o código da capacete: '))
                        quant = int(input('Quantas unidades:  '))
                        capacetes[cod] = {
    'marca': marca,
    'modelo': modelo,
    'valor': valor,
    'quantidade': quant
} 
                        print('Produto cadastrado com sucesso!')
                    
                    elif q == 3:
                        marca = input('Digite a marca da sapatilha: ')
                        modelo = input('Digite o modelo da sapatilha: ')
                        valor= float(input('Digite o valor da sapatilha: '))
                        cod= str(input('Digite o código da sapatilha: '))
                        quant = int(input('Quantas unidades:  '))
                        sapatilhas[cod] = {
    'marca': marca,
    'modelo': modelo,
    'valor': valor,
    'quantidade': quant
}
                        print('Produto cadastrado com sucesso!')
                    elif q == 4:
                        marca = input('Digite a marca da roupa: ')
                        valor= float(input('Digite o valor da roupa: '))
                        tam = input('Digite o tamanho da roupa: ').upper()
                        cod = input('Digite o código da roupa: ')
                        quant = int(input('Quantas unidades:  '))
                        roupas[cod] = {
    'marca': marca,
    'tamanho': tam,
    'valor': valor,
    'quantidade': quant
} 
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
                            print('Código:', codigo)
                            print('Marca:', bicicletas[codigo]['marca'])
                            print('Modelo:', bicicletas[codigo]['modelo'])
                            print('Valor: R$', bicicletas[codigo]['valor'])
                            print('Quantidade:', bicicletas[codigo]['quantidade'])
                    elif q == 2:
                        for codigo in capacetes:
                            print('--------------------')
                            print('Código:', codigo)
                            print('Marca:', capacetes[codigo]['marca'])
                            print('Modelo:', capacetes[codigo]['modelo'])
                            print('Valor: R$', capacetes[codigo]['valor'])
                            print('Quantidade:', capacetes[codigo]['quantidade'])
                    elif q == 3:
                        for codigo in sapatilhas:
                            print('--------------------')
                            print('Código:', codigo)
                            print('Marca:', sapatilhas[codigo]['marca'])
                            print('Modelo:', sapatilhas[codigo]['modelo'])
                            print('Valor: R$', sapatilhas[codigo]['valor'])
                            print('Quantidade:', sapatilhas[codigo]['quantidade'])
                    elif q == 4:
                        for codigo in roupas:
                            print('--------------------')
                            print('Código:', codigo)
                            print('Marca:', roupas[codigo]['marca'])
                            print('Tamanho:', roupas[codigo]['tamanho'])
                            print('Valor: R$', roupas[codigo]['valor'])
                            print('Quantidade:', roupas[codigo]['quantidade'])
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
                                print(bicicletas[cod]['marca'])
                                print(bicicletas[cod]['modelo'])
                                print(bicicletas[cod]['valor']1)
                                print(bicicletas[cod]['quantidade'])
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
                                    bicicletas[cod]["marca"] = nova_marca
                                elif q == 2:
                                    novo_modelo = input('Digite o novo modelo da bicicleta: ')
                                    bicicletas[cod]["modelo"] = novo_modelo
                                elif q == 3:
                                    novo_valor = float(input('Digite o novo valor: R$ '))
                                    bicicletas[cod]["valor"] = novo_valor
                                elif q == 4:
                                    nova_quant = int(input('Digite a nova quantidade no estoque: '))
                                    bicicletas[cod]["quantidade"] = nova_quant
                                elif q == 5:
                                    novo_cod = input('Novo código: ')
                                    bicicletas[novo_cod] = bicicletas[cod]
                                    del bicicletas[cod]

                    elif q == 2:
                                codigo = input('Digite o código do capacete: ')

                                if codigo in capacetes:
                                    print('### CAPACETE ENCONTRADO ###')
                                    print('-----------------------')
                                    print(capacetes[cod]['marca'])
                                    print(capacetes[cod]['modelo'])
                                    print(capacetes[cod]['valor']1)
                                    print(capacetes[cod]['quantidade'])
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
                                        capacetes[codigo]['marca'] = nova_marca
                                    elif q == 2:
                                        novo_modelo = input('Digite o novo modelo desejado: ')
                                        capacetes[codigo]['modelo'] = novo_modelo
                                    elif q == 3:
                                        novo_valor = float(input('Digite o novo valor: '))
                                        capacetes[codigo]['valor'] = novo_valor
                                    elif q == 4:
                                        nova_quant = int(input('Digite o novo preço deseja: '))
                                        capacetes[codigo]['quantidade'] = nova_quant
                                    elif q == 5:
                                        novo_cod= input('Digite o novo códgio do produto: ')
                                        capacetes[novo_cod] = capacetes[codigo]
                                        del capacetes[codigo]

                    elif q == 3:
                                codigo = input('Digite o código da sapatilha: ')

                                if codigo in sapatilhas:
                                    print('### CAPACETE ENCONTRADO ###')
                                    print('-----------------------')
                                    print(sapatilhas[cod]['marca'])
                                    print(sapatilhas[cod]['modelo'])
                                    print(sapatilhas[cod]['valor']1)
                                    print(sapatilhas[cod]['quantidade'])
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
                                        sapatilhas[codigo]['marca'] = nova_marca

                                    elif q == 2:
                                        novo_modelo = input('Digite o novo modelo desejado: ')
                                        sapatilhas[codigo]['modelo'] = novo_modelo

                                    elif q == 3:
                                        novo_valor = float(input('Digite o novo valor: '))
                                        sapatilhas[codigo]['valor'] = novo_valor

                                    elif q == 4:
                                        nova_quant = int(input('Digite o novo preço deseja: '))
                                        sapatilhas[codigo]['quantidade'] = nova_quant

                                    elif q == 5:
                                        novo_cod= input('Digite o novo códgio do produto: ')
                                        sapatilhas[novo_cod] = sapatilhas[codigo]
                                        del sapatilhas[codigo]
                    elif q == 5:
                            codigo = input('Digite o código da roupa: ')

                            if codigo in sapatilhas:
                                    print('### CAPACETE ENCONTRADO ###')
                                    print('-----------------------')
                                    print(sapatilhas[cod]['marca'])
                                    print(sapatilhas[cod]['modelo'])
                                    print(sapatilhas[cod]['valor']1)
                                    print(sapatilhas[cod]['quantidade'])
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
                                        roupas[codigo]['marca'] = nova_marca

                                    elif q == 2:
                                        novo_tamanho = input('Digite o tamanho: ').upper()
                                        roupas[codigo]['tamanho'] = novo_tamanho

                                    elif q == 3:
                                        novo_valor = float(input('Digite o novo valor : '))
                                        roupas[codigo]['valor'] = novo_valor

                                    elif q == 4:
                                        nova_quant = int(input('Digite o novo preço deseja: '))
                                        roupas[codigo]['quantidade'] = nova_quant

                                    elif q == 5:
                                        novo_cod= input('Digite o novo códgio do produto: ')
                                        roupas[novo_cod] = roupas[codigo]
                                        del roupas[codigo]
                                                            
            elif q == 4:
                os.system("clear")
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
                os.system("clear")
                remover = str(input('Digite o código do produto que você deseja deletar: '))
                for produto in estoque:
                    if produto['codigo'] == remover:
                        print('### PRODUTO ENCONTRADO ###')
                        certeza = input('TEM CERTEZA QUE DESEJA DELETAR [S/N]:').upper()
                        if certeza == 'S':
                            print('DELETANDO PRODUTO')
                            estoque.remove(produto)
                        
    elif resp == 2:
        os.system("clear")
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
        os.system("clear")
        print('''
###############################################
############ 1 - NOVA VENDA            ########
############ 2 - HISTÓRICO DE VENDAS   ########      
############ 3 - BUSCAR VENDAS         ########     
############ 4 - VOLTAR                ########       
              ''')
        q = int(input('Qual opção você deseja: '))
    
    elif resp == 4:
        os.system("clear")
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
##### PROGRAMA ENCERRADO #####
              ''')
    else:
        print('OPÇÃO INVÁLIDA')
    
