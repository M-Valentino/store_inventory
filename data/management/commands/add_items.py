from django.core.management.base import BaseCommand
from data.models import Item
from data.constants import Categories
from django.utils import timezone


class Command(BaseCommand):
    help = 'Adds 20 grocery items to the database'

    def handle(self, *args, **kwargs):
        items_data = [
        {"name": "Organic Bananas", "category": Categories.PRODUCE, "upc": "040000001234", "qty": 50,
         "description": "Fresh organic bananas, naturally grown without pesticides, rich in potassium and perfect for smoothies or snacks. Ideal for maintaining energy levels and supporting heart health in a natural way."},
        
        {"name": "Whole Milk 1 Gallon", "category": Categories.DAIRY, "upc": "070123456789", "qty": 30,
         "description": "A gallon of whole milk, rich in calcium and vitamin D, perfect for your daily dairy needs. Whether in coffee, cereal, or cooking, it provides creamy texture and essential nutrients for strong bones."},
        
        {"name": "Free-Range Eggs", "category": Categories.DAIRY, "upc": "070123456790", "qty": 40,
         "description": "Fresh free-range eggs, sourced from chickens raised in humane conditions with space to roam. Ideal for breakfast or baking, offering a rich flavor and packed with protein and essential vitamins."},
        
        {"name": "Almond Butter", "category": Categories.PANTRY, "upc": "080012345678", "qty": 25,
         "description": "Creamy almond butter made from high-quality roasted almonds. A healthy alternative to peanut butter, packed with protein, fiber, and healthy fats. Perfect for spreading on toast or adding to smoothies."},
        
        {"name": "Quinoa", "category": Categories.PANTRY, "upc": "080012345679", "qty": 35,
         "description": "Nutritious quinoa, a versatile superfood high in protein, fiber, and essential amino acids. A gluten-free grain, perfect for salads, side dishes, or as a base for your favorite healthy recipes."},
        
        {"name": "Chicken Breast", "category": Categories.MEAT, "upc": "090987654321", "qty": 15,
         "description": "Lean, tender chicken breast, perfect for grilling, baking, or stir-frying. A great source of protein, low in fat, and versatile for a variety of meals. Ideal for maintaining a balanced diet."},
        
        {"name": "Ground Beef", "category": Categories.MEAT, "upc": "090987654322", "qty": 20,
         "description": "Fresh ground beef, ideal for burgers, tacos, or meatballs. A versatile protein option, perfect for a variety of dishes. Packed with iron and B vitamins to support energy levels and overall health."},
        
        {"name": "Salmon Fillets", "category": Categories.SEAFOOD, "upc": "100012345678", "qty": 18,
         "description": "Fresh, high-quality salmon fillets, rich in omega-3 fatty acids for heart and brain health. Perfect for grilling, baking, or pan-searing, these fillets are flavorful and packed with essential nutrients."},
        
        {"name": "Shrimp (Frozen)", "category": Categories.SEAFOOD, "upc": "100012345679", "qty": 22,
         "description": "Frozen shrimp, peeled and deveined for convenience. A low-calorie, high-protein seafood option that's perfect for quick stir-fries, pasta, or salads. Sustainably sourced and full of flavor."},
        
        {"name": "Broccoli Crowns", "category": Categories.PRODUCE, "upc": "040000002345", "qty": 45,
         "description": "Fresh broccoli crowns, packed with vitamins C, K, and fiber. Perfect for steaming, roasting, or adding to stir-fries. A healthy, low-calorie vegetable option that supports a strong immune system."},
        
        {"name": "Sweet Potatoes", "category": Categories.PRODUCE, "upc": "040000003456", "qty": 60,
         "description": "Nutritious sweet potatoes, rich in fiber, vitamins A and C, and antioxidants. Perfect for roasting, mashing, or baking into fries. A great addition to any meal, supporting immune function and skin health."},
        
        {"name": "Greek Yogurt", "category": Categories.DAIRY, "upc": "070123456791", "qty": 50,
         "description": "Creamy Greek yogurt, high in protein and probiotics. Perfect for a healthy snack, smoothie base, or breakfast addition. Supports gut health and provides a rich source of calcium and essential nutrients."},
        
        {"name": "Orange Juice 1L", "category": Categories.BEVERAGES, "upc": "110012345678", "qty": 35,
         "description": "Refreshing orange juice made from 100% pure oranges. Packed with vitamin C to boost your immune system, this 1-liter bottle is perfect for breakfast or as a refreshing drink throughout the day."},
        
        {"name": "Bottled Water (12 Pack)", "category": Categories.BEVERAGES, "upc": "110012345679", "qty": 25,
         "description": "Convenient 12-pack of bottled water. Perfect for hydration on the go, whether for work, the gym, or outdoor activities. Clean, pure water to keep you refreshed and hydrated throughout your day."},
        
        {"name": "Spaghetti", "category": Categories.PANTRY, "upc": "120012345678", "qty": 40,
         "description": "Classic spaghetti pasta, made from high-quality durum wheat. Perfect for pairing with your favorite sauces, whether traditional marinara or creamy alfredo. A pantry staple for quick and delicious meals."},
        
        {"name": "Tomato Sauce", "category": Categories.PANTRY, "upc": "120012345679", "qty": 38,
         "description": "Rich and flavorful tomato sauce, perfect for pasta dishes, pizzas, or as a base for soups and stews. Made from ripe, high-quality tomatoes, offering a perfect balance of sweetness and acidity."},
        
        {"name": "Cheddar Cheese", "category": Categories.DAIRY, "upc": "070123456792", "qty": 28,
         "description": "Sharp cheddar cheese, perfect for snacking, cooking, or adding to sandwiches. Rich in calcium and protein, this cheese offers a bold flavor that pairs well with crackers, burgers, and more."},
        
        {"name": "Bacon", "category": Categories.MEAT, "upc": "090987654323", "qty": 15,
         "description": "Crispy, flavorful bacon, perfect for breakfast, sandwiches, or adding to salads. Made from high-quality pork, this bacon provides a savory, rich taste that's hard to resist, whether cooked crispy or soft."},
        
        {"name": "Frozen Peas", "category": Categories.FROZEN, "upc": "130012345678", "qty": 27,
         "description": "Frozen peas, perfect for adding to soups, stews, or side dishes. A nutritious and convenient vegetable option, rich in vitamins and fiber. Ready to use straight from the freezer with no prep required."},
        
        {"name": "Vanilla Ice Cream", "category": Categories.FROZEN, "upc": "130012345679", "qty": 20,
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
