from django.test import TestCase
from django.urls import reverse
from data.models import Item
import base64
from urllib.parse import quote

class ExtendedInfoViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Item.objects.create(name='Apples (Gala)', category='Produce', upc='123456789012', qty=10, description='These are sweet apples.')
        Item.objects.create(name='Salmon Filets', category='Seafood', upc='123456789013', qty=5, description='Yummy Fish.')

    def test_get_description(self):
        response = self.client.get(reverse('extendedInfo'), {'upc': '123456789012'})
        self.assertEqual(response.status_code, 200)
        # ID is automatically added with SQLite and increments starting at 1.
        expected_response = {"message": 'These are sweet apples.', "id": 1}
        self.assertEqual(response.json(), expected_response, 'An existing product should have its description returned.')

    def test_update_description(self):
        url = reverse('extendedInfo')
        description = 'Lorem ipsum. test test'
        encoded_description = base64.b64encode(quote(description).encode('utf-8')).decode('utf-8')
        
        response = self.client.post(
            url, 
            data={'upc': '123456789013', 'description': encoded_description}
        )
        self.assertEqual(response.status_code, 200)
        expected_response = {"message": "success", "new_description": "Lorem ipsum. test test"}
        self.assertEqual(response.json(), expected_response, 'A product with an existing UPC can be updated with a new description.')
