
from django.urls import path
from .views import homepage, contact, error_404_view, faq, about
urlpatterns = [
    path('', homepage, name = 'home'),
    path('contact/', contact, name = 'contact'),
    path('404/', error_404_view, name = 'error'),
    path('about/', about, name = 'about'),
    path('faq/', faq, name = 'faq')
]
