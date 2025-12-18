from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('product/<int:product_id>/', views.single_product, name='single_product'),
    path('product/<slug:slug>/', views.single_product_by_slug, name='single_product_slug'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('compare/', views.compare, name='compare'),
]

