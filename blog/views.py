from django.shortcuts import render, get_object_or_404
from .models import BlogPost, BlogCategory

# Create your views here.

def blog_list(request):
    """Blog listing page"""
    return render(request, 'blog-single.html')

def blog_category(request, slug):
    """Blog posts by category"""
    category = get_object_or_404(BlogCategory, slug=slug, is_active=True)
    return render(request, 'blog-single.html', {'category': category})

def blog_single(request, blog_id):
    """Single blog post page"""
    post = get_object_or_404(BlogPost, id=blog_id, status='published')
    post.increment_views()
    return render(request, 'blog-single.html', {'post': post})

def blog_single_by_slug(request, slug):
    """Single blog post page by slug"""
    post = get_object_or_404(BlogPost, slug=slug, status='published')
    post.increment_views()
    return render(request, 'blog-single.html', {'post': post})