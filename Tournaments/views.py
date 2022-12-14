from django.shortcuts import render
from .models import Tournament

# Create your views here.

def home_view(request):
    tournaments=Tournament.objects.all()
    return render(request,"home.html")