from django.test import TestCase
import requests
import json
# dados precisam ser alterados a cada teste, especialmente email e cpf
class TestesRequisicoesPOSTUsuarios(TestCase):

    def setUp(self):
        self.URL = "http://127.0.0.1:8000/users/"

        self.newUser = {
            "name": "Barbara",
            "Email": "barbie@gmail.com",
            "password": "1234",
            "cpf": "27919782082",
            "birthdate": "2022-06-22",
            "fone": "88 99974-8741",
            "cep": "69874-222",
            "description": "Testando 123"
        }


    def test_post_valid_user(self):
        response = requests.post(self.URL, json=self.newUser)
        self.assertEquals(response.status_code, 400)

    def test_post_invalid_cpf_user(self):
        self.newUser['cpf'] = "231.853.560-47"
        response = requests.post(self.URL, json=self.newUser)
        self.assertEquals(response.status_code, 400)

    def test_post_invalid_birthdate_user(self):
        self.newUser['birthdate'] = "06-22-2022"
        response = requests.post(self.URL, json=self.newUser)
        self.assertEquals(response.status_code, 400)