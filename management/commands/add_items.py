from django.core.management.base import BaseCommand
from your_app_name.models import Item
from django.utils import timezone

class Command(BaseCommand):
    help = 'Adds 20 grocery items to the database'

    def handle(self, *args, **kwargs):
        items_data = [
            {"name": "Organic Bananas", "category": "Produce", "upc": "040000001234", "qty": 50},
            {"name": "Whole Milk 1 Gallon", "category": "Dairy", "upc": "070123456789", "qty": 30},
            {"name": "Free-Range Eggs", "category": "Dairy", "upc": "070123456790", "qty": 40},
            {"name": "Almond Butter", "category": "Pantry", "upc": "080012345678", "qty": 25},
            {"name": "Quinoa", "category": "Pantry", "upc": "080012345679", "qty": 35},
            {"name": "Chicken Breast", "category": "Meat", "upc": "090987654321", "qty": 15},
            {"name": "Ground Beef", "category": "Meat", "upc": "090987654322", "qty": 20},
            {"name": "Salmon Fillets", "category": "Seafood", "upc": "100012345678", "qty": 18},
            {"name": "Shrimp (Frozen)", "category": "Seafood", "upc": "100012345679", "qty": 22},
            {"name": "Broccoli Crowns", "category": "Produce", "upc": "040000002345", "qty": 45},
            {"name": "Sweet Potatoes", "category": "Produce", "upc": "040000003456", "qty": 60},
            {"name": "Greek Yogurt", "category": "Dairy", "upc": "070123456791", "qty": 50},
            {"name": "Orange Juice 1L", "category": "Beverages", "upc": "110012345678", "qty": 35},
            {"name": "Bottled Water (12 Pack)", "category": "Beverages", "upc": "110012345679", "qty": 25},
            {"name": "Spaghetti", "category": "Pantry", "upc": "120012345678", "qty": 40},
            {"name": "Tomato Sauce", "category": "Pantry", "upc": "120012345679", "qty": 38},
            {"name": "Cheddar Cheese", "category": "Dairy", "upc": "070123456792", "qty": 28},
            {"name": "Bacon", "category": "Meat", "upc": "090987654323", "qty": 15},
            {"name": "Frozen Peas", "category": "Frozen", "upc": "130012345678", "qty": 27},
            {"name": "Vanilla Ice Cream", "category": "Frozen", "upc": "130012345679", "qty": 20},
        ]

        for item_data in items_data:
            Item.objects.create(
                name=item_data['name'],
                category=item_data['category'],
                upc=item_data['upc'],
                qty=item_data['qty'],
                date_added=timezone.now()
            )

        self.stdout.write(self.style.SUCCESS('Successfully added 20 grocery items to the database.'))
