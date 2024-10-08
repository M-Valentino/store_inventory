from django.db import models
from django.utils import timezone

class Item(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=10)
    upc = models.CharField(max_length=12, unique=True)
    qty = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

