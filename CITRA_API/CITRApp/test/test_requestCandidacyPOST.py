from django.test import TestCase
import requests

class TestesRequisicoesPOSTVagas(TestCase):

    def setUp(self):
        self.URL = "http://127.0.0.1:8000/candidacy/"

        self.newCandidacy = {
            "vacancyID": "8a68c45a-7a47-4c92-9be5-1e172488f33a",
            "userID": "8e1226c9-1d4c-4711-a002-f9a5093e48cb"
        }

    def test_post_valid_candidacy(self):
        response = requests.post(self.URL, json=self.newCandidacy)

        self.assertEquals(response.status_code, 201)

    def test_post_invalid_userID_candidacy(self):
        self.newCandidacy['userID'] = "8a68c45a"
        response = requests.post(self.URL, json=self.newCandidacy)

        self.assertEquals(response.status_code, 400)

    def test_post_invalid_vacancyID_candidacy(self):
        self.newCandidacy['vacancyID'] = "8a68c45a"
        response = requests.post(self.URL, json=self.newCandidacy)

        self.assertEquals(response.status_code, 400)