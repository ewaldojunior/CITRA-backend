from django.test import TestCase
import requests
import json

class TestesRequisicoesGETVagas(TestCase):

    def setUp(self):
        self.URL = "http://127.0.0.1:8000/vacancy"

    def test_get_list_vacancy(self):
        response = requests.get(self.URL)
        self.assertEquals(response.status_code, 200)

    def test_get_specific_vacancy_by_existing_name(self):
        nameV = 'pedreiro'
        queryURL = self.URL + f"?search={nameV}"
        response = requests.get(queryURL)

        self.assertEquals(response.status_code, 200)

    def test_get_specific_vacancy_by_nonexisting_name(self):
            nameV = 'nomeRandom'
            queryURL = self.URL + f"?search={nameV}"
            response = requests.get(queryURL)

            data = json.loads(response.text)

            self.assertEquals(response.status_code, 200)
            self.assertEquals(data['results'], [])

    def test_get_specific_vacancy_by_existing_company(self):
        companyV = 'Construtec'
        queryURL = self.URL + f"?search={companyV}"
        response = requests.get(queryURL)

        self.assertEquals(response.status_code, 200) 

    def test_get_specific_vacancy_by_nonexisting_company(self):
            companyV = 'Casa do Campo'
            queryURL = self.URL + f"?search={companyV}"
            response = requests.get(queryURL)

            data = json.loads(response.text)

            self.assertEquals(response.status_code, 200)
            self.assertEquals(data['results'], [])


    def test_order_vacancy_by_salary(self):
            queryURL = self.URL + f"?ordering=salary"
            response = requests.get(queryURL)

            data = json.loads(response.text)
            
            salary1 = data['results'][0]['salary']
            salary2 = data['results'][1]['salary']
            
            self.assertGreaterEqual(salary1, salary2)

