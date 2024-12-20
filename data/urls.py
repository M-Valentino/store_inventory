from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list),
    path('inventory/', views.inventory, name="inventory"),
    path('basicProductInfo/', views.basicProductInfo, name="basicProductInfo"),
    path('extendedInfo/', views.extendedInfo, name="extendedInfo"),
    path('product/', views.product, name="product"),
    path('sale/', views.sale, name="sale"),
    path('sales/', views.sales, name="sales"),
    path('restock/', views.restock, name="restock"),
]