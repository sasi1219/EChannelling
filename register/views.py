from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def register(request):
    return render(request, 'register/index.html')

