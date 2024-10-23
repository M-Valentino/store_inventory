from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from data.models import Item, Restock, Sale
import re
# TODO remove csrf_exempt when authentication implemented
from django.views.decorators.csrf import csrf_exempt
import base64
from urllib.parse import unquote
from django.utils import timezone
import json
import csv
from io import StringIO

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
        return JsonResponse({"message": item.description, "id": item.id}, status=200)
    
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
    
@csrf_exempt
@require_http_methods(["PUT"])
def sale(request):
    try:
        data = json.loads(request.body)
        id_param = data.get('id')
        sold_qty_param = int(data.get('soldQty'))
        date_sold_param = data.get('dateSold')

        current_item = Item.objects.get(id=id_param)

        if current_item.qty < sold_qty_param:
            return JsonResponse({"message": "Current quantity is too small for the QTY sold."}, status=403)

        Sale.objects.create(
            product_id=id_param,
            sold_qty=sold_qty_param,
            date_sold=date_sold_param
        )

        current_item.qty -= sold_qty_param
        current_item.save()

        return JsonResponse({'message': 'success'})

    except Item.DoesNotExist:
        return JsonResponse({'message': 'Item does not exist'}, status=404)
    except ValueError:
        return JsonResponse({'message': 'Invalid quantity provided'}, status=400)
    except Exception as e:
        return JsonResponse({'message': f'Error: {str(e)}'}, status=500)

@csrf_exempt
@require_http_methods(["PUT"])
def restock(request):
    try:
        data = json.loads(request.body)
        id_param = data.get('id')
        restock_qty_param = int(data.get('restockQty'))
        date_restocked_param = data.get('dateRestocked')

        current_item = Item.objects.get(id=id_param)

        Restock.objects.create(
            product_id=id_param,
            restock_qty=restock_qty_param,
            date_restocked=date_restocked_param
        )

        current_item.qty += restock_qty_param
        current_item.save()

        return JsonResponse({'message': 'success'})

    except Item.DoesNotExist:
        return JsonResponse({'message': 'Item does not exist'}, status=404)
    except ValueError:
        return JsonResponse({'message': 'Invalid quantity provided'}, status=400)
    except Exception as e:
        return JsonResponse({'message': f'Error: {str(e)}'}, status=500)
    
@require_http_methods(["GET"])
def sales(request):
    product_id_param = request.GET.get('productId')
    sales_data = Sale.objects.filter(product_id=product_id_param).order_by('date_sold')
    
    csv_buffer = StringIO()
    csv_writer = csv.writer(csv_buffer)
    csv_writer.writerow(['date', 'sale'])

    '''
    These are accumulation variables. There can be multiple sales on the same day, but only one sales
    value for one day is needed. Otherwise the rendered d3 chart will look unusual.
    '''
    current_duplicate_date = None
    current_qty_total_for_date = 0

    for i in range(len(sales_data)):
        sale_date = sales_data[i].date_sold
        sold_qty = sales_data[i].sold_qty

        if sale_date != current_duplicate_date:
            if current_duplicate_date is not None:
                csv_writer.writerow([current_duplicate_date.strftime('%Y-%m-%d'), current_qty_total_for_date])
            
            # Reset for the new date
            current_duplicate_date = sale_date
            current_qty_total_for_date = sold_qty
        else:
            # Accumulate for the same date
            current_qty_total_for_date += sold_qty

    if current_duplicate_date is not None:
        csv_writer.writerow([current_duplicate_date.strftime('%Y-%m-%d'), current_qty_total_for_date])

    response = HttpResponse(csv_buffer.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sales_data.csv"'
    
    return response