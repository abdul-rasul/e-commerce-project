from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('category/<slug:slug>/', views.blog_category, name='category'),
    path('<int:blog_id>/', views.blog_single, name='blog_single'),
    path('<slug:slug>/', views.blog_single_by_slug, name='blog_single_slug'),
]

