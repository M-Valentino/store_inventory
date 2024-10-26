from django.test import TestCase
from django.urls import reverse
from data.models import Item

class InventoryViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Item.objects.create(name='Apples (Gala)', category='Produce', upc='123456789012', qty=10)
        Item.objects.create(name='Salmon Filets', category='Seafood', upc='123456789013', qty=5)
        Item.objects.create(name='Oranges', category='Produce', upc='123456789014', qty=20)

    def test_inventory_returns_all_items(self):
        response = self.client.get(reverse('inventory'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3, 'Expected to receive 3 items from the inventory')

    def test_inventory_filters_by_category(self):
        response = self.client.get(reverse('inventory'), {'category': 'Produce'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2, 'Expected to receive 2 items with Produce')

    def test_inventory_search_by_name(self):
        response = self.client.get(reverse('inventory'), {'searchTerm': 'Apples', 'searchBy': 'name'})
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(len(json_response), 1, 'Expected only one item to be returned from searching by name with the search term \"Apples\".')
        self.assertIn('Apples', json_response[0]['name'], 'Search term of "Apples" should return an item containing the name "Apples"')

    def test_inventory_search_by_upc(self):
        response = self.client.get(reverse('inventory'), {'searchTerm': '123456789013', 'searchBy': 'upc'})
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(len(json_response), 1)
        self.assertEqual(json_response[0]['upc'], '123456789013', 'Expected an item returned matching the UPC provided in the search term.')

    def test_inventory_sort_by_name_ascending(self):
        response = self.client.get(reverse('inventory'), {'sortBy': 'Name Ascending'})
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(json_response[0]['name'], 'Apples (Gala)')

    def test_inventory_sort_by_qty_descending(self):
        response = self.client.get(reverse('inventory'), {'sortBy': 'QTY Descending'})
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(json_response[0]['qty'], 20, 'The first item returned with sort by QTY decending must have the highest QTY.')

    def test_inventory_returns_empty_on_invalid_search(self):
        response = self.client.get(reverse('inventory'), {'searchTerm': 'InvalidItem', 'searchBy': 'name'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 0)  # No items should be returned
