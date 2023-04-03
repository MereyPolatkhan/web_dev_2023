from django.shortcuts import render

from .models import Product, Category
from django.http import JsonResponse


# Create your views here.


def get_products(request):
    products = Product.objects.all()
    products = [p.to_json() for p in products]
    return JsonResponse(products, safe=False, json_dumps_params={"indent": 3})


def get_product(request, product_id):
    product = Product.objects.filter(pk=product_id)
    product = [p.to_json() for p in product]
    return JsonResponse(product, safe=False, json_dumps_params={"indent": 3})


def get_categories(request):
    categories = Category.objects.all()
    categories = [c.to_json() for c in categories]
    return JsonResponse(categories, safe=False, json_dumps_params={"indent": 3})


def get_category(request, category_id):
    category = Category.objects.filter(pk=category_id)
    category = [c.to_json() for c in category]
    return JsonResponse(category, safe=False, json_dumps_params={"indent": 3})


def get_category_products(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    products = [p.to_json() for p in products]
    return JsonResponse(products, safe=False, json_dumps_params={"indent": 3})
