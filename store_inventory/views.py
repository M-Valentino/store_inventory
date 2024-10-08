from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render

def homepage(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# @require_http_methods(["GET"])
def inventory(request):
  data = [
    {
        "name": "Snickers Full Size Chocolate Candy Bar",
        "upc": "040000424314",
        "count": 10
    },
    {
        "name": "Coca-Cola 12 fl oz Cans, 12 Pack",
        "upc": "049000050103",
        "count": 15
    },
    {
        "name": "Lay's Classic Potato Chips, 8 oz Bag",
        "upc": "028400040851",
        "count": 20
    },
    {
        "name": "Campbell's Chicken Noodle Soup, 10.75 oz Can",
        "upc": "051000012515",
        "count": 25
    },
    {
        "name": "Tropicana Orange Juice, 52 fl oz",
        "upc": "048500120124",
        "count": 12
    },
    ]
  return JsonResponse(data, safe=False)