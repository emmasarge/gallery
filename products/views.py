from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view show all products to search and sort """
    
    products = Product.objects.all()
    
    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
