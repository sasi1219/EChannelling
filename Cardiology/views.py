from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def Cardiology(request):
    return render(request, 'Cardiology/index.html')