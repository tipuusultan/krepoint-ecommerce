from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import time


# Create your views here.
def loginuser(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')   
        user = authenticate(username=username, password=password)
        print(username,password)
        if user is not None:
            login(request , user)
            return redirect('/')
        else:
            return redirect('/account/login')

    return render(request, 'app/login.html')






def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            messages.warning(request, "Passwod Does not match")
        else:
            print('user created')
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            messages.success(request, "Your Account has been Created Succesfully")
            return redirect('/account/login')

        
    context = {
        'form':"form"
    }

    return render(request, 'app/customerregistration.html' , context)


def logout_view(request):
    logout(request)
    return redirect('/account/login')


def forgetpassword(request):
    return render(request, 'account/forgetpassword.html')
