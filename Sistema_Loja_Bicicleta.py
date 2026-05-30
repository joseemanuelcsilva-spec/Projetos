resp = ' '
lista = []
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
                        marca_bike = input('Digite a marca da Bicicleta: ')
                        modelo_bike = input('Digite o modelo da Bicicleta: ')
                        valor_bike = int(input('Digite o valor da Bicicleta: '))
                        codigo_bike = int(input('Digite o código da Bicicleta: '))
                        quant_bike = int(input('Quantas unidades: '))

                    elif q == 2:
                        marca_capacete = input('Digite a marca da capacete: ')
                        modelo_capacete = input('Digite o modelo da capacete: ')
                        valor_capacete = int(input('Digite o valor da capacete: '))
                        codigo_capacete = int(input('Digite o código da capacete: '))
                        quant_capacete = int(input('Quantas unidades:  '))
                    
                    elif q == 3:
                        marca_sapatilha = input('Digite a marca da sapatilha: ')
                        modelo_sapatilha = input('Digite o modelo da sapatilha: ')
                        valor_sapatilha = int(input('Digite o valor da sapatilha: '))
                        codigo_sapatilha = int(input('Digite o código da sapatilha: '))
                        quant_sapatilha = int(input('Quantas unidades:  '))
                    elif q == 4:
                        marca_roupa = input('Digite a marca da sapatilha: ')
                        modelo_roupa = input('Digite o modelo da sapatilha: ')
                        valor_roupa = int(input('Digite o valor da sapatilha: '))
                        codigo_roupa = int(input('Digite o código da sapatilha: '))
                        quant_roupa = int(input('Quantas unidades:  '))
                
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
                        print('''
CÓDIGO: XXXXX
MARCA: XXXXXX
MODELO: XXXXXX
VALOR: XXXXX
QUANTIDADE: XXXX
                          ''')


                    elif q == 2:
                        print('LISTANDO TODOS OS CAPACETES DO ESTOQUE.....')
                        print('''
CÓDIGO: XXXXX
MARCA: XXXXXX
MODELO: XXXXXX
VALOR: XXXXX
QUANTIDADE: XXXX
                          ''')


                    elif q == 3:
                        print('LISTANDO TODAS AS SAPATILHAS DO ESTOQUE.....')
                        print('''
CÓDIGO: XXXXX
MARCA: XXXXXX
MODELO: XXXXXX
VALOR: XXXXX
QUANTIDADE: XXXX
                          ''')

                    elif q == 4:
                        print('LISTANDO TODAS AS ROUPAS DE CICLISMO.....')
                        print('''
CÓDIGO: XXXXX
MARCA: XXXXXX
MODELO: XXXXXX
VALOR: XXXXX
QUANTIDADE: XXXX
                          ''')
            elif q == 3:
                cod = int(input('Digite o código do produto: '))

                if cod in lista : # CASO O PRODUTO ESTEJA NO ESTOQUE 
                    print('''
Produto encontrado:
CÓDIGO: XXXX
Marca: XXXX
MODELO : XXXX
VALOR: XXXX
QUANTIDADE: 
                          ''')
                    
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
                        q = int(input('Qual opção você deseja?'))
                        if q == 1:
                            marc = input('DIgite a marca: ')
                        elif q == 2:
                            mod = input('Digite o modelo: ')
                        elif q == 3:
                            preco = float(input('Digite o valor:R$ '))
                        elif q == 4:
                            quantidade = int(input('Digite a quantidade: '))
                        elif q == 5:
                            new_cod = int('DIgite o novo código: ')
            
            elif q == 4:
                print('VOCÊ ENTROU NO MODO DE PESQUISA: ')
                codigo = int(input('DIGITE O CÓDIGO DO PRODUTO'))
                if codigo in lista: #VERIFICANDO SE O CÓDIGO DO PRODUTO VAI ESTA NA LISTA
                    print('''
### PRODUTO ENCONTRADO ###
                          
CÓDIGO: XXXX
Marca: XXXX
MODELO : XXXX
VALOR: XXXX
QUANTIDADE: 
                          ''')
                else:
                    print('### PRODUTO NÃO ENCONTRADO ###')

            elif q == 5:
                remove = int(input('DIGITE O CÓDIGO DO PRODUTO QUE VOCÊ DESEJA DELETAR: '))
                crtz = input('TEM CERTEZA QUE QUER DELETAR ESSE PRODUTO [S/N]:').upper()

                if crtz == 'S':
                    print('DELETANDO PRODUTO')
                else:
                    remove2 = int(input('DIGITE O CÓDIGO CORRETO DO PRODUTO QUE VOCÊ DESEJA DELETAR: '))
                    print('DELETANDO PRODUTO')
            

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
### PROJETO DA DISCIPLINA DCT1101                           ###
### TEMA: SISTEMA DE GERENCIAMENTO DE UMA LOJA DE BICICLETA ###
### DOCENTE RESPONSÁVEL: FLAVIUS GORGÔNIO                   ###
### DISCENTE: JOSÉ EMANUEL DA CÂMARA SILVA                  ### 
              ''')
    elif resp == 0:
        print('''
##### PROGRAMA ENCERRADO #####
              ''')
    else:
        print('OPÇÃO INVÁLIDA')
    

