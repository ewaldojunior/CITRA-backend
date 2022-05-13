import re
from validate_docbr import CPF

def cpf_valido(numero_CPF):
    cpf = CPF()
    return cpf.validate(numero_CPF)

def nome_valido(nome):
    return nome.isalpha()

def celular_valido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta

    