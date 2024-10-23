from django.core.management.base import BaseCommand
from data.models import Item, Sale
from data.constants import Categories
from django.utils import timezone
from datetime import datetime


class Command(BaseCommand):
    help = 'Adds 20 grocery items to the database'

    def handle(self, *args, **kwargs):
        items_data = [
        {"name": "Organic Bananas", "category": Categories.PRODUCE, "upc": "040000001234", "qty": 100,
         "description": "Fresh organic bananas, naturally grown without pesticides, rich in potassium and perfect for smoothies or snacks. Ideal for maintaining energy levels and supporting heart health in a natural way."},
        
        {"name": "Whole Milk 1 Gallon", "category": Categories.DAIRY, "upc": "070123456789", "qty": 80,
         "description": "A gallon of whole milk, rich in calcium and vitamin D, perfect for your daily dairy needs. Whether in coffee, cereal, or cooking, it provides creamy texture and essential nutrients for strong bones."},
        
        {"name": "Free-Range Eggs", "category": Categories.DAIRY, "upc": "070123456790", "qty": 70,
         "description": "Fresh free-range eggs, sourced from chickens raised in humane conditions with space to roam. Ideal for breakfast or baking, offering a rich flavor and packed with protein and essential vitamins."},
        
        {"name": "Almond Butter", "category": Categories.PANTRY, "upc": "080012345678", "qty": 75,
         "description": "Creamy almond butter made from high-quality roasted almonds. A healthy alternative to peanut butter, packed with protein, fiber, and healthy fats. Perfect for spreading on toast or adding to smoothies."},
        
        {"name": "Quinoa", "category": Categories.PANTRY, "upc": "080012345679", "qty": 50,
         "description": "Nutritious quinoa, a versatile superfood high in protein, fiber, and essential amino acids. A gluten-free grain, perfect for salads, side dishes, or as a base for your favorite healthy recipes."},
        
        {"name": "Chicken Breast", "category": Categories.MEAT, "upc": "090987654321", "qty": 60,
         "description": "Lean, tender chicken breast, perfect for grilling, baking, or stir-frying. A great source of protein, low in fat, and versatile for a variety of meals. Ideal for maintaining a balanced diet."},
        
        {"name": "Ground Beef", "category": Categories.MEAT, "upc": "090987654322", "qty": 50,
         "description": "Fresh ground beef, ideal for burgers, tacos, or meatballs. A versatile protein option, perfect for a variety of dishes. Packed with iron and B vitamins to support energy levels and overall health."},
        
        {"name": "Salmon Fillets", "category": Categories.SEAFOOD, "upc": "100012345678", "qty": 60,
         "description": "Fresh, high-quality salmon fillets, rich in omega-3 fatty acids for heart and brain health. Perfect for grilling, baking, or pan-searing, these fillets are flavorful and packed with essential nutrients."},
        
        {"name": "Shrimp (Frozen)", "category": Categories.SEAFOOD, "upc": "100012345679", "qty": 80,
         "description": "Frozen shrimp, peeled and deveined for convenience. A low-calorie, high-protein seafood option that's perfect for quick stir-fries, pasta, or salads. Sustainably sourced and full of flavor."},
        
        {"name": "Broccoli Crowns", "category": Categories.PRODUCE, "upc": "040000002345", "qty": 70,
         "description": "Fresh broccoli crowns, packed with vitamins C, K, and fiber. Perfect for steaming, roasting, or adding to stir-fries. A healthy, low-calorie vegetable option that supports a strong immune system."},
        
        {"name": "Sweet Potatoes", "category": Categories.PRODUCE, "upc": "040000003456", "qty": 65,
         "description": "Nutritious sweet potatoes, rich in fiber, vitamins A and C, and antioxidants. Perfect for roasting, mashing, or baking into fries. A great addition to any meal, supporting immune function and skin health."},
        
        {"name": "Greek Yogurt", "category": Categories.DAIRY, "upc": "070123456791", "qty": 80,
         "description": "Creamy Greek yogurt, high in protein and probiotics. Perfect for a healthy snack, smoothie base, or breakfast addition. Supports gut health and provides a rich source of calcium and essential nutrients."},
        
        {"name": "Orange Juice 1L", "category": Categories.BEVERAGES, "upc": "110012345678", "qty": 90,
         "description": "Refreshing orange juice made from 100% pure oranges. Packed with vitamin C to boost your immune system, this 1-liter bottle is perfect for breakfast or as a refreshing drink throughout the day."},
        
        {"name": "Bottled Water (12 Pack)", "category": Categories.BEVERAGES, "upc": "110012345679", "qty": 120,
         "description": "Convenient 12-pack of bottled water. Perfect for hydration on the go, whether for work, the gym, or outdoor activities. Clean, pure water to keep you refreshed and hydrated throughout your day."},
        
        {"name": "Spaghetti", "category": Categories.PANTRY, "upc": "120012345678", "qty": 50,
         "description": "Classic spaghetti pasta, made from high-quality durum wheat. Perfect for pairing with your favorite sauces, whether traditional marinara or creamy alfredo. A pantry staple for quick and delicious meals."},
        
        {"name": "Tomato Sauce", "category": Categories.PANTRY, "upc": "120012345679", "qty": 55,
         "description": "Rich and flavorful tomato sauce, perfect for pasta dishes, pizzas, or as a base for soups and stews. Made from ripe, high-quality tomatoes, offering a perfect balance of sweetness and acidity."},
        
        {"name": "Cheddar Cheese", "category": Categories.DAIRY, "upc": "070123456792", "qty": 70,
         "description": "Sharp cheddar cheese, perfect for snacking, cooking, or adding to sandwiches. Rich in calcium and protein, this cheese offers a bold flavor that pairs well with crackers, burgers, and more."},
        
        {"name": "Bacon", "category": Categories.MEAT, "upc": "090987654323", "qty": 40,
         "description": "Crispy, flavorful bacon, perfect for breakfast, sandwiches, or adding to salads. Made from high-quality pork, this bacon provides a savory, rich taste that's hard to resist, whether cooked crispy or soft."},
        
        {"name": "Frozen Peas", "category": Categories.FROZEN, "upc": "130012345678", "qty": 100,
         "description": "Frozen peas, perfect for adding to soups, stews, or side dishes. A nutritious and convenient vegetable option, rich in vitamins and fiber. Ready to use straight from the freezer with no prep required."},
        
        {"name": "Vanilla Ice Cream", "category": Categories.FROZEN, "upc": "130012345679", "qty": 40,
         "description": "Creamy vanilla ice cream, made with real vanilla beans for a rich and smooth flavor. A perfect treat for any occasion, whether served in a cone, with toppings, or as a base for sundaes and desserts."},
        ]

        for item_data in items_data:
            Item.objects.create(
                name=item_data['name'],
                category=item_data['category'],
                upc=item_data['upc'],
                qty=item_data['qty'],
                date_added=timezone.now(),
                description=item_data['description']
            )

        self.stdout.write(self.style.SUCCESS('Successfully added 20 grocery items to the database.'))

        sales_data = [
            {"product_id": 1, "sold_qty": 20, "date_sold": datetime(2024, 1, 7)},
            {"product_id": 1, "sold_qty": 15, "date_sold": datetime(2024, 2, 14)},
            {"product_id": 1, "sold_qty": 18, "date_sold": datetime(2024, 3, 22)},
            {"product_id": 1, "sold_qty": 22, "date_sold": datetime(2024, 4, 9)},
            {"product_id": 1, "sold_qty": 17, "date_sold": datetime(2024, 5, 16)},
            {"product_id": 1, "sold_qty": 21, "date_sold": datetime(2024, 6, 26)},
            {"product_id": 1, "sold_qty": 19, "date_sold": datetime(2024, 7, 30)},
            {"product_id": 1, "sold_qty": 14, "date_sold": datetime(2024, 8, 8)},
            {"product_id": 1, "sold_qty": 23, "date_sold": datetime(2024, 9, 12)},
            {"product_id": 1, "sold_qty": 16, "date_sold": datetime(2024, 9, 28)},

            {"product_id": 2, "sold_qty": 11, "date_sold": datetime(2024, 1, 10)},
            {"product_id": 2, "sold_qty": 7, "date_sold": datetime(2024, 2, 15)},
            {"product_id": 2, "sold_qty": 14, "date_sold": datetime(2024, 3, 20)},
            {"product_id": 2, "sold_qty": 10, "date_sold": datetime(2024, 4, 25)},
            {"product_id": 2, "sold_qty": 5, "date_sold": datetime(2024, 5, 5)},
            {"product_id": 2, "sold_qty": 16, "date_sold": datetime(2024, 6, 10)},
            {"product_id": 2, "sold_qty": 8, "date_sold": datetime(2024, 7, 5)},
            {"product_id": 2, "sold_qty": 12, "date_sold": datetime(2024, 8, 15)},
            {"product_id": 2, "sold_qty": 9, "date_sold": datetime(2024, 9, 1)},
            {"product_id": 2, "sold_qty": 6, "date_sold": datetime(2024, 9, 20)},

            {"product_id": 3, "sold_qty": 13, "date_sold": datetime(2024, 1, 12)},
            {"product_id": 3, "sold_qty": 10, "date_sold": datetime(2024, 2, 18)},
            {"product_id": 3, "sold_qty": 8, "date_sold": datetime(2024, 3, 24)},
            {"product_id": 3, "sold_qty": 18, "date_sold": datetime(2024, 4, 10)},
            {"product_id": 3, "sold_qty": 12, "date_sold": datetime(2024, 5, 22)},
            {"product_id": 3, "sold_qty": 7, "date_sold": datetime(2024, 6, 8)},
            {"product_id": 3, "sold_qty": 15, "date_sold": datetime(2024, 7, 18)},
            {"product_id": 3, "sold_qty": 6, "date_sold": datetime(2024, 8, 21)},
            {"product_id": 3, "sold_qty": 14, "date_sold": datetime(2024, 9, 3)},
            {"product_id": 3, "sold_qty": 11, "date_sold": datetime(2024, 9, 25)},

            {"product_id": 4, "sold_qty": 17, "date_sold": datetime(2024, 1, 8)},
            {"product_id": 4, "sold_qty": 6, "date_sold": datetime(2024, 2, 5)},
            {"product_id": 4, "sold_qty": 9, "date_sold": datetime(2024, 3, 28)},
            {"product_id": 4, "sold_qty": 19, "date_sold": datetime(2024, 4, 3)},
            {"product_id": 4, "sold_qty": 10, "date_sold": datetime(2024, 5, 30)},
            {"product_id": 4, "sold_qty": 14, "date_sold": datetime(2024, 6, 22)},
            {"product_id": 4, "sold_qty": 11, "date_sold": datetime(2024, 7, 25)},
            {"product_id": 4, "sold_qty": 8, "date_sold": datetime(2024, 8, 10)},
            {"product_id": 4, "sold_qty": 13, "date_sold": datetime(2024, 9, 9)},
            {"product_id": 4, "sold_qty": 16, "date_sold": datetime(2024, 9, 27)},

            {"product_id": 5, "sold_qty": 15, "date_sold": datetime(2024, 1, 4)},
            {"product_id": 5, "sold_qty": 12, "date_sold": datetime(2024, 2, 6)},
            {"product_id": 5, "sold_qty": 14, "date_sold": datetime(2024, 3, 15)},
            {"product_id": 5, "sold_qty": 9, "date_sold": datetime(2024, 4, 23)},
            {"product_id": 5, "sold_qty": 6, "date_sold": datetime(2024, 5, 12)},
            {"product_id": 5, "sold_qty": 10, "date_sold": datetime(2024, 6, 4)},
            {"product_id": 5, "sold_qty": 18, "date_sold": datetime(2024, 7, 2)},
            {"product_id": 5, "sold_qty": 13, "date_sold": datetime(2024, 8, 11)},
            {"product_id": 5, "sold_qty": 17, "date_sold": datetime(2024, 9, 5)},
            {"product_id": 5, "sold_qty": 8, "date_sold": datetime(2024, 9, 28)},

            {"product_id": 6, "sold_qty": 16, "date_sold": datetime(2024, 1, 20)},
            {"product_id": 6, "sold_qty": 9, "date_sold": datetime(2024, 2, 24)},
            {"product_id": 6, "sold_qty": 20, "date_sold": datetime(2024, 3, 30)},
            {"product_id": 6, "sold_qty": 5, "date_sold": datetime(2024, 4, 17)},
            {"product_id": 6, "sold_qty": 14, "date_sold": datetime(2024, 5, 9)},
            {"product_id": 6, "sold_qty": 10, "date_sold": datetime(2024, 6, 19)},
            {"product_id": 6, "sold_qty": 13, "date_sold": datetime(2024, 7, 24)},
            {"product_id": 6, "sold_qty": 6, "date_sold": datetime(2024, 8, 2)},
            {"product_id": 6, "sold_qty": 17, "date_sold": datetime(2024, 9, 6)},
            {"product_id": 6, "sold_qty": 12, "date_sold": datetime(2024, 9, 29)},

            {"product_id": 7, "sold_qty": 21, "date_sold": datetime(2024, 1, 22)},
            {"product_id": 7, "sold_qty": 10, "date_sold": datetime(2024, 2, 9)},
            {"product_id": 7, "sold_qty": 15, "date_sold": datetime(2024, 3, 13)},
            {"product_id": 7, "sold_qty": 8, "date_sold": datetime(2024, 4, 5)},
            {"product_id": 7, "sold_qty": 18, "date_sold": datetime(2024, 5, 14)},
            {"product_id": 7, "sold_qty": 9, "date_sold": datetime(2024, 6, 30)},
            {"product_id": 7, "sold_qty": 14, "date_sold": datetime(2024, 7, 12)},
            {"product_id": 7, "sold_qty": 5, "date_sold": datetime(2024, 8, 6)},
            {"product_id": 7, "sold_qty": 11, "date_sold": datetime(2024, 9, 15)},
            {"product_id": 7, "sold_qty": 17, "date_sold": datetime(2024, 9, 21)},

            {"product_id": 8, "sold_qty": 12, "date_sold": datetime(2024, 1, 25)},
            {"product_id": 8, "sold_qty": 8, "date_sold": datetime(2024, 2, 12)},
            {"product_id": 8, "sold_qty": 11, "date_sold": datetime(2024, 3, 29)},
            {"product_id": 8, "sold_qty": 7, "date_sold": datetime(2024, 4, 11)},
            {"product_id": 8, "sold_qty": 16, "date_sold": datetime(2024, 5, 18)},
            {"product_id": 8, "sold_qty": 5, "date_sold": datetime(2024, 6, 29)},
            {"product_id": 8, "sold_qty": 14, "date_sold": datetime(2024, 7, 20)},
            {"product_id": 8, "sold_qty": 9, "date_sold": datetime(2024, 8, 27)},
            {"product_id": 8, "sold_qty": 13, "date_sold": datetime(2024, 9, 11)},
            {"product_id": 8, "sold_qty": 22, "date_sold": datetime(2024, 9, 30)},

            {"product_id": 9, "sold_qty": 13, "date_sold": datetime(2024, 1, 9)},
            {"product_id": 9, "sold_qty": 17, "date_sold": datetime(2024, 2, 22)},
            {"product_id": 9, "sold_qty": 8, "date_sold": datetime(2024, 3, 19)},
            {"product_id": 9, "sold_qty": 6, "date_sold": datetime(2024, 4, 13)},
            {"product_id": 9, "sold_qty": 11, "date_sold": datetime(2024, 5, 4)},
            {"product_id": 9, "sold_qty": 15, "date_sold": datetime(2024, 6, 6)},
            {"product_id": 9, "sold_qty": 12, "date_sold": datetime(2024, 7, 8)},
            {"product_id": 9, "sold_qty": 14, "date_sold": datetime(2024, 8, 22)},
            {"product_id": 9, "sold_qty": 19, "date_sold": datetime(2024, 9, 4)},
            {"product_id": 9, "sold_qty": 10, "date_sold": datetime(2024, 9, 28)},

            {"product_id": 10, "sold_qty": 15, "date_sold": datetime(2024, 1, 6)},
            {"product_id": 10, "sold_qty": 7, "date_sold": datetime(2024, 2, 27)},
            {"product_id": 10, "sold_qty": 16, "date_sold": datetime(2024, 3, 12)},
            {"product_id": 10, "sold_qty": 9, "date_sold": datetime(2024, 4, 8)},
            {"product_id": 10, "sold_qty": 14, "date_sold": datetime(2024, 5, 26)},
            {"product_id": 10, "sold_qty": 11, "date_sold": datetime(2024, 6, 11)},
            {"product_id": 10, "sold_qty": 18, "date_sold": datetime(2024, 7, 9)},
            {"product_id": 10, "sold_qty": 13, "date_sold": datetime(2024, 8, 25)},
            {"product_id": 10, "sold_qty": 20, "date_sold": datetime(2024, 9, 14)},
            {"product_id": 10, "sold_qty": 12, "date_sold": datetime(2024, 9, 26)},

            {"product_id": 11, "sold_qty": 10, "date_sold": datetime(2024, 1, 28)},
            {"product_id": 11, "sold_qty": 9, "date_sold": datetime(2024, 2, 17)},
            {"product_id": 11, "sold_qty": 7, "date_sold": datetime(2024, 3, 21)},
            {"product_id": 11, "sold_qty": 19, "date_sold": datetime(2024, 4, 26)},
            {"product_id": 11, "sold_qty": 15, "date_sold": datetime(2024, 5, 11)},
            {"product_id": 11, "sold_qty": 14, "date_sold": datetime(2024, 6, 15)},
            {"product_id": 11, "sold_qty": 13, "date_sold": datetime(2024, 7, 19)},
            {"product_id": 11, "sold_qty": 5, "date_sold": datetime(2024, 8, 29)},
            {"product_id": 11, "sold_qty": 18, "date_sold": datetime(2024, 9, 7)},
            {"product_id": 11, "sold_qty": 6, "date_sold": datetime(2024, 9, 29)},

            {"product_id": 12, "sold_qty": 11, "date_sold": datetime(2024, 1, 23)},
            {"product_id": 12, "sold_qty": 8, "date_sold": datetime(2024, 2, 7)},
            {"product_id": 12, "sold_qty": 12, "date_sold": datetime(2024, 3, 3)},
            {"product_id": 12, "sold_qty": 17, "date_sold": datetime(2024, 4, 6)},
            {"product_id": 12, "sold_qty": 14, "date_sold": datetime(2024, 5, 15)},
            {"product_id": 12, "sold_qty": 9, "date_sold": datetime(2024, 6, 23)},
            {"product_id": 12, "sold_qty": 19, "date_sold": datetime(2024, 7, 1)},
            {"product_id": 12, "sold_qty": 10, "date_sold": datetime(2024, 8, 18)},
            {"product_id": 12, "sold_qty": 13, "date_sold": datetime(2024, 9, 8)},
            {"product_id": 12, "sold_qty": 6, "date_sold": datetime(2024, 9, 22)},

            {"product_id": 13, "sold_qty": 22, "date_sold": datetime(2024, 1, 27)},
            {"product_id": 13, "sold_qty": 13, "date_sold": datetime(2024, 2, 8)},
            {"product_id": 13, "sold_qty": 6, "date_sold": datetime(2024, 3, 2)},
            {"product_id": 13, "sold_qty": 14, "date_sold": datetime(2024, 4, 28)},
            {"product_id": 13, "sold_qty": 15, "date_sold": datetime(2024, 5, 21)},
            {"product_id": 13, "sold_qty": 8, "date_sold": datetime(2024, 6, 3)},
            {"product_id": 13, "sold_qty": 16, "date_sold": datetime(2024, 7, 21)},
            {"product_id": 13, "sold_qty": 12, "date_sold": datetime(2024, 8, 5)},
            {"product_id": 13, "sold_qty": 17, "date_sold": datetime(2024, 9, 10)},
            {"product_id": 13, "sold_qty": 7, "date_sold": datetime(2024, 9, 24)},

            {"product_id": 14, "sold_qty": 12, "date_sold": datetime(2024, 1, 19)},
            {"product_id": 14, "sold_qty": 5, "date_sold": datetime(2024, 2, 25)},
            {"product_id": 14, "sold_qty": 9, "date_sold": datetime(2024, 3, 11)},
            {"product_id": 14, "sold_qty": 18, "date_sold": datetime(2024, 4, 30)},
            {"product_id": 14, "sold_qty": 14, "date_sold": datetime(2024, 5, 8)},
            {"product_id": 14, "sold_qty": 7, "date_sold": datetime(2024, 6, 28)},
            {"product_id": 14, "sold_qty": 11, "date_sold": datetime(2024, 7, 6)},
            {"product_id": 14, "sold_qty": 20, "date_sold": datetime(2024, 8, 1)},
            {"product_id": 14, "sold_qty": 13, "date_sold": datetime(2024, 9, 17)},
            {"product_id": 14, "sold_qty": 10, "date_sold": datetime(2024, 9, 29)},

            {"product_id": 15, "sold_qty": 14, "date_sold": datetime(2024, 1, 21)},
            {"product_id": 15, "sold_qty": 8, "date_sold": datetime(2024, 2, 3)},
            {"product_id": 15, "sold_qty": 10, "date_sold": datetime(2024, 3, 16)},
            {"product_id": 15, "sold_qty": 17, "date_sold": datetime(2024, 4, 1)},
            {"product_id": 15, "sold_qty": 9, "date_sold": datetime(2024, 5, 27)},
            {"product_id": 15, "sold_qty": 13, "date_sold": datetime(2024, 6, 7)},
            {"product_id": 15, "sold_qty": 7, "date_sold": datetime(2024, 7, 16)},
            {"product_id": 15, "sold_qty": 16, "date_sold": datetime(2024, 8, 4)},
            {"product_id": 15, "sold_qty": 11, "date_sold": datetime(2024, 9, 13)},
            {"product_id": 15, "sold_qty": 6, "date_sold": datetime(2024, 9, 28)},

            {"product_id": 16, "sold_qty": 11, "date_sold": datetime(2024, 1, 26)},
            {"product_id": 16, "sold_qty": 14, "date_sold": datetime(2024, 2, 28)},
            {"product_id": 16, "sold_qty": 5, "date_sold": datetime(2024, 3, 10)},
            {"product_id": 16, "sold_qty": 18, "date_sold": datetime(2024, 4, 7)},
            {"product_id": 16, "sold_qty": 12, "date_sold": datetime(2024, 5, 1)},
            {"product_id": 16, "sold_qty": 9, "date_sold": datetime(2024, 6, 25)},
            {"product_id": 16, "sold_qty": 16, "date_sold": datetime(2024, 7, 22)},
            {"product_id": 16, "sold_qty": 6, "date_sold": datetime(2024, 8, 9)},
            {"product_id": 16, "sold_qty": 13, "date_sold": datetime(2024, 9, 19)},
            {"product_id": 16, "sold_qty": 10, "date_sold": datetime(2024, 9, 27)},

            {"product_id": 17, "sold_qty": 15, "date_sold": datetime(2024, 1, 30)},
            {"product_id": 17, "sold_qty": 10, "date_sold": datetime(2024, 2, 21)},
            {"product_id": 17, "sold_qty": 8, "date_sold": datetime(2024, 3, 7)},
            {"product_id": 17, "sold_qty": 14, "date_sold": datetime(2024, 4, 4)},
            {"product_id": 17, "sold_qty": 19, "date_sold": datetime(2024, 5, 7)},
            {"product_id": 17, "sold_qty": 13, "date_sold": datetime(2024, 6, 16)},
            {"product_id": 17, "sold_qty": 6, "date_sold": datetime(2024, 7, 7)},
            {"product_id": 17, "sold_qty": 17, "date_sold": datetime(2024, 8, 23)},
            {"product_id": 17, "sold_qty": 9, "date_sold": datetime(2024, 9, 16)},
            {"product_id": 17, "sold_qty": 11, "date_sold": datetime(2024, 9, 26)},

            {"product_id": 18, "sold_qty": 22, "date_sold": datetime(2024, 1, 13)},
            {"product_id": 18, "sold_qty": 12, "date_sold": datetime(2024, 2, 23)},
            {"product_id": 18, "sold_qty": 5, "date_sold": datetime(2024, 3, 8)},
            {"product_id": 18, "sold_qty": 9, "date_sold": datetime(2024, 4, 29)},
            {"product_id": 18, "sold_qty": 14, "date_sold": datetime(2024, 5, 2)},
            {"product_id": 18, "sold_qty": 17, "date_sold": datetime(2024, 6, 14)},
            {"product_id": 18, "sold_qty": 10, "date_sold": datetime(2024, 7, 4)},
            {"product_id": 18, "sold_qty": 7, "date_sold": datetime(2024, 8, 3)},
            {"product_id": 18, "sold_qty": 13, "date_sold": datetime(2024, 9, 18)},
            {"product_id": 18, "sold_qty": 8, "date_sold": datetime(2024, 9, 30)},

            {"product_id": 19, "sold_qty": 11, "date_sold": datetime(2024, 1, 18)},
            {"product_id": 19, "sold_qty": 6, "date_sold": datetime(2024, 2, 16)},
            {"product_id": 19, "sold_qty": 14, "date_sold": datetime(2024, 3, 23)},
            {"product_id": 19, "sold_qty": 9, "date_sold": datetime(2024, 4, 2)},
            {"product_id": 19, "sold_qty": 16, "date_sold": datetime(2024, 5, 13)},
            {"product_id": 19, "sold_qty": 12, "date_sold": datetime(2024, 6, 18)},
            {"product_id": 19, "sold_qty": 7, "date_sold": datetime(2024, 7, 13)},
            {"product_id": 19, "sold_qty": 10, "date_sold": datetime(2024, 9, 2)},
            {"product_id": 19, "sold_qty": 13, "date_sold": datetime(2024, 9, 28)},

            {"product_id": 20, "sold_qty": 10, "date_sold": datetime(2024, 1, 5)},
            {"product_id": 20, "sold_qty": 8, "date_sold": datetime(2024, 2, 10)},
            {"product_id": 20, "sold_qty": 12, "date_sold": datetime(2024, 3, 15)},
            {"product_id": 20, "sold_qty": 9, "date_sold": datetime(2024, 4, 20)},
            {"product_id": 20, "sold_qty": 14, "date_sold": datetime(2024, 5, 25)},
            {"product_id": 20, "sold_qty": 11, "date_sold": datetime(2024, 6, 5)},
            {"product_id": 20, "sold_qty": 13, "date_sold": datetime(2024, 7, 12)},
            {"product_id": 20, "sold_qty": 10, "date_sold": datetime(2024, 8, 17)},
            {"product_id": 20, "sold_qty": 15, "date_sold": datetime(2024, 9, 22)},
            {"product_id": 20, "sold_qty": 9, "date_sold": datetime(2024, 9, 29)},
        ]

        for sale_data in sales_data:
            Sale.objects.create(
                product_id=sale_data['product_id'],
                sold_qty=sale_data['sold_qty'],
                date_sold=sale_data['date_sold']
            )
        self.stdout.write(self.style.SUCCESS('Successfully sale data for grocery items.'))