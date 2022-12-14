from django.shortcuts import render

# Create your views here.

def login_view(request):
    return render(request,"login.html")

def add_view(request):
    return render(request,"add_staff.html")

