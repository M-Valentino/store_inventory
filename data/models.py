from django.db import models
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=10)
    upc = models.CharField(max_length=12, unique=True)
    qty = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)
    description = models.CharField(max_length=300, default="")

class Sale(models.Model):
    product_id = models.IntegerField()
    sold_qty = models.IntegerField()
    date_sold = models.DateTimeField(default=timezone.now)

class Restock(models.Model):
    product_id = models.IntegerField()
    restock_qty = models.IntegerField()
    date_restocked = models.DateTimeField(default=timezone.now)