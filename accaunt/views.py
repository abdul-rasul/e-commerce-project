from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.

def login_view(request):
    """User login page - redirect to Django admin login or use custom form"""
    if request.user.is_authenticated:
        return redirect('accaunt:my_account')
    return render(request, 'login.html')

def register(request):
    """User registration page"""
    if request.user.is_authenticated:
        return redirect('accaunt:my_account')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('accaunt:my_account')
    else:
        form = UserCreationForm()
    
    return render(request, 'login.html', {'form': form, 'register': True})

@login_required
def my_account(request):
    """User account/profile page"""
    return render(request, 'my-account.html')
