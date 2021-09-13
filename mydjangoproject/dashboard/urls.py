from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registerform', views.registerForm, name='registerform'),
    path('register', views.register, name='register'),
    path('loginform', views.loginForm, name='loginform'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]