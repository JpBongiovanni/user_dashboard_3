from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages

def index(request):
    return render(request, 'home_page.html')

def sign_in_render(request):
    return render(request, 'sign_in.html')

def register_render(request):
    return render(request, 'register.html')

def admin_dashboard_render(request):
    return render(request, 'admin_dashboard.html')

def user_information_render(request):
    return render(request, 'user_information.html')

def register(request):
    if request.method == "GET":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        if len(User.objects.all()) == 0:
            user_level = 9
            return redirect('admin_dashboard_render')
        else:
            user_level = 1
        return redirect('user_information_render')
        

def login(request):
    if request.method == "GET":
        return redirect('/')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    request.session['user_email'] = user.email
    messages.success(request, "You have successfully logged in!")
    if User.objects.user_level == 9:
        return redirect('admin_dashboard_render')
    else:
        return redirect('user_information_render')