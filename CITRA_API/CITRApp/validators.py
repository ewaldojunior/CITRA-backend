import re
from validate_docbr import CPF
from pycep_correios import get_address_from_cep, WebService, exceptions

def cpf_valido(numero_CPF):
    cpf = CPF()
    return cpf.validate(numero_CPF)

def cep_valido(numero_CEP):
    modelo = '[0-9]{5}-[0-9]{3}'
    resposta = re.findall(modelo, numero_CEP)
    return resposta


def celular_valido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta

    