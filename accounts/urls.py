from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginuser, name='login'),
    path('register/', views.register, name='customerregistration'),
    path('logout/', views.logout_view, name='logout'),
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),

]
