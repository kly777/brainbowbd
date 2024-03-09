from django.test import TestCase

# Create your tests here.
import requests
import pprint

payload = {
    'username': 'kk',
    'password': '2580'
}

response = requests.post('http://127.0.0.1:9000/api/sign/signin/', data=payload)

pprint.pprint(response.json())
