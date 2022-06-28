from typing_extensions import Self
from django.test import TestCase
from CITRApp.serializers import VacancySerializer
from CITRApp.models import Vacancy, User


class TestVacancySerializer(TestCase):

    def setUp(self):
        self.user_attributes = {
            "name": "Isanio",
            "Email": "isanioV@gmail.com",
            "password": "1234",
            "cpf": "07242780365",
            "birthdate": "2022-06-22",
            "fone": "88 99974-8741",
            "picture": None,
            "cv": None,
            "cep": "69874-222",
            "description": "Testando 123"
        }

        self.user = User.objects.create(**self.user_attributes)

        self.vacancy_attributes = {
            "nameVacancy": "Pedreiro",
            "nameCompany": "Construtec",
            "shifts": "T",
            "fone": "88 98122-9880",
            "cep": "63900-049",
            "salary": 1200.0,
            "picture": None,
            "typeHires": "",
            "description": "Vaga teste",
            "userIdVacancy": self.user
        }



        self.vacancy = Vacancy.objects.create(**self.vacancy_attributes)
        self.serializer = VacancySerializer(instance=self.vacancy)
    
    def test_campos_esperados(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(["vacancyId",
                                            "nameVacancy",
                                            "nameCompany",
                                            "shifts",
                                            "fone",
                                            "cep",
                                            "salary",
                                            "picture",
                                            "typeHires",
                                            "description",
                                            "userIdVacancy"]))
