from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list),
    path('inventory/', views.inventory, name="inventory")
]