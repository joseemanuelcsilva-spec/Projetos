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
############ 0 - SAIR                  ########
          ''')
    resp = int(input('Qual opção você deseja: '))
    if resp == 1:
        print('''
         GERENCIAMENTO DE ESTOQUE 
###############################################
############ 1 - CADASTRAR PRODUTO     ########
############ 2 - LISTAR PRODUTOS       ########      
############ 3 - ATUALIZAR ESTOQUE     ########     
############ 4 - BUSCAR PRODUTO        ########
############ 5 - REMOVER PRODUTO       ########
############ 6 - VOLTAR                ########            
              ''')
        q = int(input('Qual opção você deseja: '))

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
    

