from django.shortcuts import render

# Create your views here.

def cart(request):
    """Shopping cart page"""
    return render(request, 'cart.html')

def checkout(request):
    """Checkout page"""
    return render(request, 'checkout.html')

def empty_cart(request):
    """Empty cart page"""
    return render(request, 'empty-cart.html')