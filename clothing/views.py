from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'clothing/home.html')

def women(request):
    return render(request, 'clothing/women.html')

def men(request):
    return render(request, 'clothing/men.html')