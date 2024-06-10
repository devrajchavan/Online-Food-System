from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'onlineFood/home.html')
