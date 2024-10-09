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
    categories_param = request.GET.get('category')

    if categories_param:
        categories = [cat.strip() for cat in categories_param.split(',')]  # Split and strip whitespace
        items = Item.objects.filter(category__in=categories).values("name", "category", "upc", "qty")
    else:
        items = Item.objects.all().values("name", "category", "upc", "qty")

    items_list = list(items)
    return JsonResponse(items_list, safe=False)
