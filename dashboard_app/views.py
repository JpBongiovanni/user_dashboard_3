from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'home_page.html')

def sign_in_render(request):
    return render(request, 'sign_in.html')