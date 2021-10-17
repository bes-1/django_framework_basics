import datetime
import os

from django.shortcuts import render
from products.models import ProductCategory, Product


# Create your views here.
def index(request):
    date_val = datetime.datetime.now()
    context = {
        'title': 'GeekShop',
        'date': date_val,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
