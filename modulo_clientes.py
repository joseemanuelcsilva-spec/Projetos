def menu_clientes():
        resp = ' '
        if resp == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
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
                                            cod = novo_codigo
                                            print('Código alterado com sucesso!')
                        else:
                            print('CLIENTE NÃO ENCONTRADO')
                        
                    elif q == 5:
                        print('''
    ###########################                          
    ##### DELETAR CADASTRO ####
    ###########################                          
                            ''')
                        codigo = input('Digite o código do cliente que você deseja deletar: ')
                        if codigo in clientes:
                            crtz = input('Tem certeza que deseja deletar o cliente [S/N]: ').upper()
                            if crtz == 'S':
                                print('REMOVENDO CLIENTE ...')
                                time.sleep(2)
                                print('CLIENTE REMOVIDO')
                                del clientes[codigo]
                            else:
                                codigo = input('Digite o codigo correto do cliente para remover: ') 
                                del clientes[codigo]
                        else:
                            print('### CLIENTE NÃO ENCONTRADO ###')