from django.contrib import messages, auth
from django.shortcuts import render, redirect

# Create your views here.
from dashboard.models import User


def index(request):
    return render(request, 'dashboard/index.html')

def registerForm(request):
    return render(request, 'auth/registration.html')

def register(request):
    print(request.POST)
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(name=name, password=password, email=email, phone=phone)
        user.save()
        messages.success(request, 'You are now registered and can log in')
        return redirect('login')
    else:
        return render(request, 'auth/login.html')

def loginForm(request):
    return render(request, 'auth/login.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'auth/login.html')

def logout(request):
    return render(request, 'auth/registration.html')



