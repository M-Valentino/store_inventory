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
    search_param = request.GET.get('search')

    categories = [cat.strip() for cat in categories_param.split(',')] if categories_param else []

    items = Item.objects.filter(category__in=categories) if categories else Item.objects.all()
    
    if search_param:
        items = items.filter(name__icontains=search_param)

    items_list = list(items.values("name", "category", "upc", "qty"))
    return JsonResponse(items_list, safe=False)
