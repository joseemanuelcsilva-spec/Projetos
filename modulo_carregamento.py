def carregar_bicicletas():
    bicicletas = {}
    try:
        arq_bicicletas = open("bicicletas.txt", "rt", encoding="utf-8")
        for linha in arq_bicicletas:
            linha = linha.strip()
            if linha != "":
                dados = linha.split(",")
                codigo = dados[0]
                marca = dados[1]
                modelo = dados[2]
                valor = float(dados[3])
                quantidade = int(dados[4])
                bicicletas[codigo] = [marca, modelo, valor, quantidade]
        arq_bicicletas.close()
    except:
        bicicletas = {
            'b001':['caloi', 'adv', 200, 3],
            'b002':['caloi', 'advsasas', 200, 3]
        }
        print("Arquivo não encontrado.")
        arq_bicicletas = open("bicicletas.txt", "wt", encoding="utf-8")
        for codigo, dados in bicicletas.items():
            arq_bicicletas.write(
                f"{codigo},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n"
            )
        arq_bicicletas.close()
    
def carregar_capacetes():
    capacetes = {}
    try:
        arq_capacetes = open("capacetes.txt", "rt", encoding="utf-8")
        for linha in arq_capacetes:
            linha = linha.strip()
            if linha != "":
                dados = linha.split(",")
                codigo = dados[0]
                marca = dados[1]
                modelo = dados[2]
                valor = float(dados[3])
                quantidade = int(dados[4])
                capacetes[codigo] = [marca, modelo, valor, quantidade]
        arq_capacetes.close()

    except:
        capacetes = {
            'c001':['Oggi', 'Superlight', 299,9, 10]
        }
        print("Arquivo de capacetes não encontrado.")
        arq_capacetes = open("capacetes.txt", "wt", encoding="utf-8")
        for codigo, dados in capacetes.items():
            arq_capacetes.write(
                f"{codigo},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n"
            )
        arq_capacetes.close()
def carregar_sapatilhas():
    sapatilhas = {}
    try:
        arq_sapatilhas = open("sapatilhas.txt", "rt", encoding="utf-8")
        for linha in arq_sapatilhas:
            linha = linha.strip()
            if linha != "":
                dados = linha.split(",")
                codigo = dados[0]
                marca = dados[1]
                modelo = dados[2]
                valor = float(dados[3])
                quantidade = int(dados[4])
                sapatilhas[codigo] = [marca, modelo, valor, quantidade]
        arq_sapatilhas.close()

    except:
        print("Arquivo de sapatilhas não encontrado.")
        arq_sapatilhas = open("sapatilhas.txt", "wt", encoding="utf-8")
        for codigo, dados in sapatilhas.items():
            arq_sapatilhas.write(
                f"{codigo},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n"
            )
        arq_sapatilhas.close()
def carregar_roupas():
    roupas = {}
    try:
        arq_roupas = open("roupas.txt", "rt", encoding="utf-8")

        for linha in arq_roupas:
            linha = linha.strip()
            if linha != "":
                dados = linha.split(",")
                codigo = dados[0]
                marca = dados[1]
                tamanho = dados[2]
                valor = float(dados[3])
                quantidade = int(dados[4])
                roupas[codigo] = [marca, tamanho, valor, quantidade]
        arq_roupas.close()

    except:
        print("Arquivo de roupas não encontrado.")
        arq_roupas = open("roupas.txt", "wt", encoding="utf-8")
        for codigo, dados in roupas.items():
            arq_roupas.write(
                f"{codigo},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n"
            )
        arq_roupas.close()
def carregar_clientes():
    clientes = {}
    try:
        arq_clientes = open("clientes.txt", "rt", encoding="utf-8")
        for linha in arq_clientes:
            linha = linha.strip()
            if linha != "":
                dados = linha.split(",")
                codigo = dados[0]
                nome = dados[1]
                sobrenome = dados[2]
                telefone = dados[3]
                cpf = dados[4]
                clientes[codigo] = [
                    nome,
                    sobrenome,
                    telefone,
                    cpf
                ]

        arq_clientes.close()

    except:
        print("Arquivo de clientes não encontrado.")
        rq_clientes = open("clientes.txt", "wt", encoding="utf-8")
        for codigo, dados in clientes.items():
            arq_clientes.write(
                f"{codigo},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n"
            )
        arq_clientes.close()
def carregar_vendas():
    vendas = {}
    try:
        arq_vendas = open("vendas.txt", "rt", encoding="utf-8")
        for linha in arq_vendas:
            linha = linha.strip()
            if linha != "":
                dados = linha.split(",")
                cod_venda = dados[0]
                cod_cliente = dados[1]
                nome = dados[2]
                produto = dados[3]
                valor = float(dados[4])
                pagamento = dados[5]
                data_hora = dados[6]
                status = dados[7]
                vendas[cod_venda] = [
                    cod_cliente,
                    nome,
                    produto,
                    valor,
                    pagamento,
                    data_hora,
                    status
                ]
        arq_vendas.close()
    except:
        print("Arquivo de vendas não encontrado.")
        arq_vendas = open("vendas.txt", "wt", encoding="utf-8")
        for codigo, dados in vendas.items():
            arq_vendas.write(
                f"{codigo},{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]},{dados[5]},{dados[6]},{dados[7]}\n"
            )
        arq_vendas.close()