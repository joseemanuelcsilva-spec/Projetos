import os
import time
from modulo_validacao import validar_cpf, validar_celular
def menu_clientes(clientes):
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
                        print('Validando Número....')
                        time.sleep(2)
                        while not validar_celular(tel):
                            print('Numero InValido')
                            tel = input('Digite o telefone do cliente; xx xxxxx-xxxx ')
                            print('Validando numero')
                            time.sleep(2)
                        print('Número válido')
                        cpf = input('Digite o cpf do cliente (Apenas Números): ')
                        print('Validando cpf')
                        time.sleep(2)
                        while not validar_cpf(cpf):
                            print('CPF INvalido')
                            cpf = input('Digite o cpf do cliente (Apenas Números): ')
                            print('Validando cpf')
                            time.sleep(2)
                        print('CPf Validado')
                        cod = input('Digite o código do cliente: ').upper()
                        status = 'ATIVO'
                        clientes[cod] = [nome, sobrenome, tel, cpf, status]
                        print('CLIENTE CADASTRADO COM SUCESSO')
                    elif q == 2:
                        print('LISTANDO OS CLIENTES ....')
                        for cod in clientes:
                            print('Codigo:', cod)
                            print('Nome:', clientes[cod][0])
                            print('Sobrenome:', clientes[cod][1])
                            print('Telefone:', clientes[cod][2])
                            print('CPF:', clientes[cod][3])
                            print('Status:', clientes[cod][4])
                            print('-------------------------------------')
                    elif q == 3:
                        print('''
#############################                             
##### PESQUISAR CLIENTE #####
#############################
                            ''')
                        cod = input('Digite o código do cliente: ').upper()
                        if cod in clientes:
                            print('### CLIENTE ENCONTRADO ###')
                            print('-------------------------------------')
                            print('Código:', cod) 
                            print('Nome:', clientes[cod][0])
                            print('Sobrenome:',clientes[cod][1])
                            print('Telefone:', clientes[cod][2])
                            print('CPF:', clientes[cod][3])
                            print('Status:', clientes[cod][4])
                            print('-------------------------------------')
                        else:
                            print('#### CLIENTE NÃO FOI ENCONTRADO ####')
                    elif q == 4:
                        print('''
###############################
#### MÓDULO DE ATUALIZAÇÃO ####
###############################
                            ''')
                        cod = input('Digite o código do cliente: ').upper()
                        if cod in clientes:
                            print(
                                '### CLIENTE ENCONTRADO ###')
                            print('-------------------------------------')
                            print('Codigo:',cod) 
                            print('Nome:', clientes[cod][0])
                            print('Sobrenome:',clientes[cod][1])
                            print('Telefone:', clientes[cod][2])
                            print('CPF:', clientes[cod][3])
                            print('-------------------------------------')
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
                                            novo_nome = input('Digite o novo nome: ')
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
                                            cod = novo_codigo
                                            print('Código alterado com sucesso!')
                        else:
                            print('CLIENTE NÃO ENCONTRADO')
                    elif q == 5:
                        print('''
############################                          
##### DESATIVAR CLIENTE ####
############################                          
                            ''')
                        codigo = input('Digite o código do cliente que você deseja desativar: ').upper()
                        if codigo in clientes:
                            crtz = input('Tem certeza que deseja desativar o cliente [S/N]: ').upper()
                            if crtz == 'S':
                                print('DESATIVANDO O CLIENTE ...')
                                time.sleep(2)
                                print('CLIENTE DESATIVADO')
                                clientes[cod][4] ='DESATIVADO'
                            else:
                                codigo = input('Digite o codigo correto do cliente para remover: ') 
                                clientes[cod][4] ='DESATIVADO'
                        else:
                            print('### CLIENTE NÃO ENCONTRADO ###')
        return clientes