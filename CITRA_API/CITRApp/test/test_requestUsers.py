from django.test import TestCase
import requests
import json

class TestesRequisicoesUsuario(TestCase):

    def setUp(self):
        self.URL = "http://127.0.0.1:8000/users"

    def test_get_list_users(self):
        response = requests.get(self.URL)
        self.assertEquals(response.status_code, 200)

 #   def test_get_specific_user_by_name(self):
 #       name = 'Isanio'
 #       queryURL = self.URL + f"?results=[name={name}]"
 #       response = requests.get(queryURL)

 #       userdata = json.loads(response.text)

#        print(userdata)
#        self.assertEquals(response.status_code, 200)
