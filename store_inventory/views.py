from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render

def homepage(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@require_http_methods(["GET"])
def inventory(request):
  data = {
        "Name": "Snickers Full Size Chocolate Candy Bar",
        "UPC": "040000424314"

    }
  return JsonResponse(data)