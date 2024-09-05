from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def blog(request):
    return render(request, 'core/blog.html')

def blog_details(request):
    return render(request, 'core/blog-details.html')

def checkout(request):
    return render(request, 'core/checkout.html')

def main(request):
    return render(request, 'core/main.html')

def shop_details(request):
    return render(request, 'core/shop-details.html')

def shop_grid(request):
    return render(request, 'core/shop-grid.html')

def shopping_cart(request):
    return render(request, 'core/shopping-cart.html')