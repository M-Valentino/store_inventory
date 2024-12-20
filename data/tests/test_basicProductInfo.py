from django.test import TestCase
from django.urls import reverse
from data.models import Item

class BasicProductInfoViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Item.objects.create(name='Apples (Gala)', category='Produce', upc='123456789012', qty=10)
        Item.objects.create(name='Salmon Filets', category='Seafood', upc='123456789013', qty=5)
        Item.objects.create(name='Oranges', category='Produce', upc='123456789014', qty=20)
        Item.objects.create(name='Chocolate Ice Cream', category='Frozen', upc='432567890123', qty=20)

    def test_update_valid_new_and_old_upc(self):
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
        self.assertEqual(response.json(), expected_response, 'A product with an existing UPC can be updated to a new UPC.')

    def test_update_valid_new_invalid_old_upc(self):
        url = reverse('basicProductInfo')
        response = self.client.post(f"{url}?oldUpc=123426789013&newUpc=223459789012")
        self.assertEqual(response.status_code, 403)
        expected_response = {"message": "Product with the provided old UPC does not exist."}
        self.assertEqual(response.json(), expected_response, 'A saved UPC that does not exist cannot be updated to a new UPC.')
        
    def test_update_upc_not_12_digits(self):
        url = reverse('basicProductInfo')
        response = self.client.post(f"{url}?oldUpc=123456789014&newUpc=22345978")
        self.assertEqual(response.status_code, 403)
        expected_response = {"message": "UPCs must be a number 12 digits long."}
        self.assertEqual(response.json(), expected_response, 'New UPCs must be 12 digits long')

    def test_update_category(self):
        url = reverse('basicProductInfo')
        response = self.client.post(f"{url}?oldUpc=432567890123&newCategory=Pantry")
        self.assertEqual(response.status_code, 200)
        expected_response = {
            "message": "success",
            "updated_item": {
                "name": 'Chocolate Ice Cream',
                "category": 'Pantry',
                "upc": "432567890123",
                "qty": 20
            }
        }
        self.assertEqual(response.json(), expected_response, 'A product with an existing UPC can be changed to a new category.')