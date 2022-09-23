from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from main.models import Users

def signin(request):

    if request.method == 'POST':
        r = request.POST
        username = r['username']
        password = r['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully entered")
            return redirect('/')
        else:
            messages.error(request, "Username or password is incorrect")
            return redirect('/sign-in/')
    else:
        return render(request, 'sign-in.html')

def signup(request):
    if request.method == 'POST':
        r = request.POST
        username = r['username']
        password = r['password']
        first_name = r['first_name']
        last_name = r['last_name']
        phone = r['phone']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully entered")
            return redirect('/sign-up/')
        else:
            Users.objects.create(username=username, password=make_password(password), first_name=first_name, last_name=last_name, phone=phone)
            messages.success(request, "Account is created successfully!")
            return redirect('/sign-in/')
    else:
        return render(request, 'sign-up.html')

def LogOut(request):
    logout(request)
    # messages.success(request, "Succes")
    return redirect('/sign-in/')