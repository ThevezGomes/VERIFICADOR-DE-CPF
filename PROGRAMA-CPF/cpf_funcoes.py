import string

def organizar_cpf(cpf):
    cpf_numeros = ""

    for i in range(len(cpf)):
        if cpf[-(i+1)] in string.digits:
            cpf_numeros += cpf[-(i+1)]
    
    return cpf_numeros
       
def decobrir_digito(cpf_numeros):

    digito = 0
    for i in range(len(cpf_numeros)):
        digito += int(cpf_numeros[i]) * (i + 2)
    
    digito = digito % 11
    if digito < 2:
        digito = 0
    else:
        digito = 11 - digito
    digito = str(digito)
    
    return digito

def finalizar_cpf(cpf):
    cpf_pronto = ""
    for caractere in cpf:
        if caractere in string.digits:
            cpf_pronto += caractere
    cpf_pronto = cpf_pronto[0:3] + "." + cpf_pronto[3:6] + "." + cpf_pronto[6:9] + "-" + cpf_pronto[9:11]
    
    return cpf_pronto

def somente_numeros(cpf):
    numeros = ""
    for caractere in cpf:
        if caractere in string.digits:
            numeros += caractere

    return numeros


                
            
