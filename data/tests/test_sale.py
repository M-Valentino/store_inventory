from django.test import TestCase
from django.urls import reverse
from data.models import Item
import json

class SaleViewTest(TestCase):

    def setUp(self):
        Item.objects.create(name='Apples', qty=10)

    def test_sale_success(self):
        url = reverse('sale')
        data = {
            'id': 1,
            'soldQty': 5,
            'dateSold': '2024-11-02'
        }
        response = self.client.put(url, json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': 'success'})
        item = Item.objects.get(pk=1)
        self.assertEqual(item.qty, 5)

    def test_sale_nonexistent_item(self):
        url = reverse('sale')
        data = {'id': 10, 'soldQty': 2, 'dateSold': '2024-11-02'}
        response = self.client.put(url, json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'message': 'Item does not exist'})

    def test_sale_insufficient_quantity(self):
        url = reverse('sale')
        data = {'id': 1, 'soldQty': 15, 'dateSold': '2024-11-02'}
        response = self.client.put(url, json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json(), {'message': 'Current quantity is too small for the QTY sold.'})

    def test_sale_invalid_quantity(self):
        url = reverse('sale')
        data = {'id': 1, 'soldQty': 'invalid', 'dateSold': '2024-11-02'}
        response = self.client.put(url, json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid quantity provided', str(response.content.decode()))
