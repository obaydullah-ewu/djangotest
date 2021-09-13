from django.contrib import messages, auth
from django.shortcuts import render, redirect
# from dashboard.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

def index(request):
    return render(request, 'dashboard/index.html')

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'H1 {username}, You are now registered and can log in')
            return render(request, 'auth/login.html')
    else:
        form = UserCreationForm()
    return render(request, 'auth/registration.html', {'form': form})

def login(request):
    # if request.method == 'POST':
    #     email = request.POST['email']
    #     password = request.POST['password']
    #
    #     user = auth.authenticate(email=email, password=password)
    #
    #     if user is not None:
    #         auth.login(request, user)
    #         messages.success(request, 'You are now logged in')
    #         return redirect('dashboard')
    #     else:
    #         messages.error(request, 'Invalid credentials')
    #         return redirect('login')
    # else:

    form = UserCreationForm()

    return render(request, 'auth/login.html', {'form': form})

def logout(request):
    return render(request, 'auth/registration.html')



