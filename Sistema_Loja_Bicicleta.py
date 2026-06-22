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
from modulo_venda import menu_venda

bicicletas = carregar_bicicletas()
capacetes = carregar_capacetes()
sapatilhas = carregar_sapatilhas()
roupas = carregar_roupas()
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
            bicicletas, capacetes, sapatilhas, roupas = menu_estoque(bicicletas, capacetes, sapatilhas, roupas)
        if resp == 2:
            clientes = menu_clientes(clientes)
        elif resp == 3:
            vendas, bicicletas, capacetes, sapatilhas, roupa, clientes = menu_venda(vendas, bicicletas, capacetes, sapatilhas, roupas, clientes)  
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
salvar_bicicletas(bicicletas)
salvar_capacetes(capacetes)
salvar_sapatilhas(sapatilhas)
salvar_roupas(roupas)
salvar_clientes(clientes)
salvar_vendas(vendas)


