from django.test import TestCase
from django.urls import reverse
from data.models import Item

class BasicProductInfoViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Item.objects.create(name='Apples (Gala)', category='Produce', upc='123456789012', qty=10)
        Item.objects.create(name='Salmon Filets', category='Seafood', upc='123456789013', qty=5)
        Item.objects.create(name='Oranges', category='Produce', upc='123456789014', qty=20)

    def test_update_upc(self):
        url = reverse('basicProductInfo')
        response = self.client.post(f"{url}?oldUpc=123456789012&newUpc=223456789012")
        self.assertEqual(response.status_code, 200)
        expected_response = {
            "message": "success",
            "updated_item": {
                "name": 'Apples (Gala)',
                "category": 'Produce',
                "upc": "223456789012",
                "qty": 10
            }
        }
        self.assertEqual(response.json(), expected_response)
        