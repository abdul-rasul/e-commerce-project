from django.urls import path
from . import views

app_name = 'accaunt'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('my-account/', views.my_account, name='my_account'),
]

