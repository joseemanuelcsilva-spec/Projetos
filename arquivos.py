bicicletas = {}
capacetes = {}
sapatilhas = {}
roupas = {}
clientes = {}
vendas = {}
def salvar_bicicletas(bicicletas):
    arq_bicicletas = open("bicicletas.txt", "wt", encoding="utf-8")
    for codigo, dados in bicicletas.items():
        arq_bicicletas.write(
            f"{codigo},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n"
        )
    arq_bicicletas.close()
    

def salvar_capacetes(capacetes):
    arq_capacetes = open("capacetes.txt", "wt", encoding="utf-8")
    for codigo, dados in capacetes.items():
        arq_capacetes.write(
            f"{codigo},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n"
        )
    arq_capacetes.close()

def salvar_sapatilhas(sapatilhas):
    arq_sapatilhas = open("sapatilhas.txt", "wt", encoding="utf-8")
    for codigo, dados in sapatilhas.items():
        arq_sapatilhas.write(
            f"{codigo},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n"
        )
    arq_sapatilhas.close()

def salvar_roupas(roupas):
    arq_roupas = open("roupas.txt", "wt", encoding="utf-8")
    for codigo, dados in roupas.items():
        arq_roupas.write(
            f"{codigo},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n"
        )
    arq_roupas.close()

def salvar_clientes(clientes):
    arq_clientes = open("clientes.txt", "wt", encoding="utf-8")
    for codigo, dados in clientes.items():
        arq_clientes.write(
            f"{codigo},{dados[0]},{dados[1]},{dados[2]},{dados[3]}\n"
        )
    arq_clientes.close()

def salvar_vendas(vendas):
    arq_vendas = open("vendas.txt", "wt", encoding="utf-8")
    for codigo, dados in vendas.items():
        arq_vendas.write(
            f"{codigo},{dados[0]},{dados[1]},{dados[2]},{dados[3]},{dados[4]},{dados[5]},{dados[6]},{dados[7]}\n"
        )
    arq_vendas.close()