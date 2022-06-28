from typing_extensions import Self
from django.test import TestCase
from CITRApp.serializers import UserSerializer
from CITRApp.models import User


class TestUserSerializer(TestCase):

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
        self.serializer = UserSerializer(instance=self.user)

    def test_campos_esperados(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(["userId",
                                                "name",
                                                "Email",
                                                "password",
                                                "cpf",
                                                "birthdate",
                                                "fone",
                                                "picture",
                                                "cv",
                                                "cep",
                                                "description"]))