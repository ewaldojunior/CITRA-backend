from django.test import TestCase
import requests
import json

class TestesRequisicoesUsuario(TestCase):

    def setUp(self):
        self.URL = "http://127.0.0.1:8000/candidacy"

    def test_get_list_candidacy(self):
        response = requests.get(self.URL)
        self.assertEquals(response.status_code, 200)
