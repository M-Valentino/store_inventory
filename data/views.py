from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from data.models import Item
# TODO remove csrf_exempt when authentication implemented
from django.views.decorators.csrf import csrf_exempt

def posts_list(request):
  return render(request, 'data/data_list.html')

@require_http_methods(["GET"])
def inventory(request):
    categories_param = request.GET.get('category')
    search_term = request.GET.get('searchTerm')
    search_by = request.GET.get('searchBy')
    sort_by = request.GET.get('sortBy')

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
          item.upc = new_upc_param

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
