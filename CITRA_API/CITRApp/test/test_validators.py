from pickle import EMPTY_SET
from typing_extensions import Self
from django.test import TestCase
from CITRApp.validators import cep_valido, celular_valido

class ValidatorsTests(TestCase):

    def teste_cep_letras(self):
        string_teste = "letras" 
        self.assertEquals([], cep_valido(string_teste))

    def teste_cep_numero_pequeno(self):
        num_teste = "0256"
        self.assertEquals([], cep_valido(num_teste))

    def teste_cep_caracteres_excedentes(self):
        num_teste = "000000000"
        self.assertEquals([], cep_valido(num_teste))

    def teste_cep_valido(self):
        num_teste = "63500-000"
        self.assertEquals(["63500-000"], cep_valido(num_teste))

    def teste_celular_letras(self):
        string_teste = "letras"
        self.assertEquals([], celular_valido(string_teste))


    def teste_celular_numero_pequeno(self):
        num_teste = "12345"
        self.assertEquals([], celular_valido(num_teste))

    def teste_celular_caracteres_excedentes(self):
        num_teste = "88 98145636363"
        self.assertEquals([], celular_valido(num_teste))

    def teste_celular_nao_formatado(self):
        num_teste = "88985226548"
        self.assertEquals([], celular_valido(num_teste))

    def teste_celular_valido(self):
        num_teste = "88 98522-6548"
        self.assertEquals(["88 98522-6548"], celular_valido(num_teste))
