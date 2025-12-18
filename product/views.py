from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.

def shop(request):
    """Shop page with product listing"""
    return render(request, 'shop-left-sidebar.html')

def category(request, slug):
    """Category page with products"""
    category = get_object_or_404(Category, slug=slug, is_active=True)
    return render(request, 'shop-left-sidebar.html', {'category': category})

def single_product(request, product_id):
    """Single product detail page"""
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'single-product.html', {'product': product})

def single_product_by_slug(request, slug):
    """Single product detail page by slug"""
    product = get_object_or_404(Product, slug=slug, status='published')
    return render(request, 'single-product.html', {'product': product})

def wishlist(request):
    """User wishlist page"""
    return render(request, 'wishlist.html')

def compare(request):
    """Product comparison page"""
    return render(request, 'compare.html')