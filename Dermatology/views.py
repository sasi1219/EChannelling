from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def Dermatology(request):
    return render(request, 'Dermatology/index.html')