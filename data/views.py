from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from data.models import Item
import re
# TODO remove csrf_exempt when authentication implemented
from django.views.decorators.csrf import csrf_exempt
import base64
from urllib.parse import unquote
from django.utils import timezone

def posts_list(request):
  return render(request, 'data/data_list.html')

@require_http_methods(["GET"])
def inventory(request):
    categories_param = request.GET.get('category')
    search_term = request.GET.get('searchTerm')
    search_by = request.GET.get('searchBy')
    sort_by = request.GET.get('sortBy')
    print(sort_by)

    categories = [cat.strip() for cat in categories_param.split(',')] if categories_param else []

    items = Item.objects.filter(category__in=categories) if categories else Item.objects.all()
    
    if search_term != '':
        if search_by == 'name':
            items = items.filter(name__icontains=search_term)
        elif search_by == 'upc':
            items = items.filter(upc__icontains=search_term)

    if sort_by == "Name Ascending":
        items = items.order_by('name')
    elif sort_by == "Name Descending":
        items = items.order_by('-name')
    elif sort_by == "UPC Ascending":
        items = items.order_by('upc')
    elif sort_by == "UPC Descending":
        items = items.order_by('-upc')
    elif sort_by == "QTY Ascending":
        items = items.order_by('qty')
    elif sort_by == "QTY Descending":
        items = items.order_by('-qty')

    items_list = list(items.values("name", "category", "upc", "qty"))
    return JsonResponse(items_list, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def basicProductInfo(request):
    old_upc_param = request.GET.get('oldUpc')
    new_upc_param = request.GET.get('newUpc')
    new_category_param = request.GET.get('newCategory')

    try:
        item = Item.objects.get(upc=old_upc_param)
    except Item.DoesNotExist:
        return JsonResponse({"message": "Product with the provided old UPC does not exist."}, status=403)

    if new_upc_param:
        itemWithNewUpcExists = Item.objects.filter(upc=new_upc_param).count()
        if itemWithNewUpcExists > 0:
            return JsonResponse({"message": "New UPC already belongs to an existing product."}, status=403)
        else:
          if re.match(r'^\d{12}$', new_upc_param):
            item.upc = new_upc_param
          else:
              return JsonResponse({"message": "UPCs must be a number 12 digits long."}, status=403)

    if new_category_param:
        item.category = new_category_param

    item.save()

    return JsonResponse({
        "message": "success",
        "updated_item": {
            "name": item.name,
            "category": item.category,
            "upc": item.upc,
            "qty": item.qty
        }
    }, safe=False)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def extendedInfo(request):
    upc_param = request.POST.get('upc') if request.method == 'POST' else request.GET.get('upc')

    try:
        item = Item.objects.get(upc=upc_param)
    except Item.DoesNotExist:
        return JsonResponse({"message": "Product with the provided UPC does not exist."}, status=404)

    if request.method == 'GET':
        return JsonResponse({"message": item.description}, status=200)
    
    elif request.method == 'POST':
        encoded_description = request.POST.get('description')
        if not encoded_description:
            return JsonResponse({"message": "No description provided."}, status=400)

        try:
            decoded_description = base64.b64decode(encoded_description).decode('utf-8') 
            decoded_description = unquote(decoded_description)
        except (ValueError, UnicodeDecodeError):
            return JsonResponse({"message": "Invalid description encoding."}, status=400)

        if len(decoded_description) <= 300:
            item.description = decoded_description
            item.save()
        else:
            return JsonResponse({"message": "Description is too long."}, status=400)
        
        return JsonResponse({"message": "success", "new_description": item.description}, status=200)
    
@csrf_exempt
@require_http_methods(["POST"])
def product(request):
    name_param = request.POST.get('name')
    upc_param = request.POST.get('upc')
    category_param = request.POST.get('category')
    description_param = request.POST.get('description')

    if not name_param or not upc_param or len(upc_param) != 12 or not category_param:
        return JsonResponse({'message': 'Invalid product information'}, status=400)
    
   
    itemWithNewUpcExists = Item.objects.filter(upc=upc_param).count()
    if itemWithNewUpcExists > 0:
      return JsonResponse({"message": "New UPC already belongs to an existing product."}, status=403)

    try:
        Item.objects.create(
            name=name_param,
            category=category_param,
            upc=upc_param,
            qty=0,
            date_added=timezone.now(),
            description=description_param
        )
        return JsonResponse({'message': 'success'})
    except Exception as e:
        return JsonResponse({'message': f'Error: {str(e)}'}, status=500)
