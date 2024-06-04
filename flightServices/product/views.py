from django.shortcuts import render
from .models import Product

# Create your views here.


def AllProducts(request):
    products = Product.objects.all()
    return render(request, "product.html", {"products": products})
