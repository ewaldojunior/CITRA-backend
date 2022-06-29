from django.test import TestCase
import requests
from CITRApp.serializers import VacancySerializer

class TestesRequisicoesPOSTVagas(TestCase):

    def setUp(self):
        self.URL = "http://127.0.0.1:8000/vacancy/"

        self.newVacancy = {
            "nameVacancy": "Engenheiro Civil",
            "nameCompany": "Casa da Construção",
            "shifts": "M",
            "fone": "88 99974-5678",
            "cep": "36987-049",
            "salary": 3850.0,
            "typeHires": "CTI",
            "description": "Vaga para Engenheiro Civil",
            "userIdVacancy": "2cbc7c30-95e8-42c0-8e32-decaebe4c1cb"
        }

    def test_post_valid_vacancy(self):
        response = requests.post(self.URL, json=self.newVacancy)

        self.assertEquals(response.status_code, 201)

    def test_post_invalid_cep(self):
        self.newVacancy['cep'] = "3698704966"

        response = requests.post(self.URL, json=self.newVacancy)

        self.assertEquals(response.status_code, 400)

    def test_post_invalid_fone(self):
        self.newVacancy['fone'] = "88 98145636363"

        response = requests.post(self.URL, json=self.newVacancy)

        self.assertEquals(response.status_code, 400)