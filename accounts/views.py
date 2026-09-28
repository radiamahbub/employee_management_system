from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.models import *

# Create your views here.
def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        user_type = request.POST.get('user_type')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            AuthUserModel.objects.create_user(
                username=username,
                email=email,
                user_type =user_type,
                password=password,
            )
            return redirect('login')
        else:
            print("Passwors doesn't match")
            
            
    return render(request,'accounts/register.html')

def login_page(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user:
                 login(request, user)
                 return redirect('dashboard')

    return render(request,'accounts/login.html')

@login_required
def dashboard_page(request):
     
     return render(request,'accounts/dashboard_base.html')

def logout_page(request):
    logout(request)
    return redirect('login')



