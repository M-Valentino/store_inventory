from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from data.models import Item

def homepage(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@require_http_methods(["GET"])
def inventory(request):
    items = Item.objects.all().values("name", "category", "upc", "qty")
    items_list = list(items)
    return JsonResponse(items_list, safe=False)