def validar_cpf(cpf):
    cpf_limpo = cpf.strip()
    if len(cpf_limpo) == 11 and cpf_limpo.isdigit():
        return True
    return False
    
def validar_celular(telefone):
    tel_limpo = telefone.strip()
    if len(tel_limpo) == 11 and tel_limpo.isdigit() and tel_limpo[0] != "0" and tel_limpo[2] == "9":
        return True
    return False