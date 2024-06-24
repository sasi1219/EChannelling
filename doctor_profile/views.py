from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def doctor_profile(request):
    return render(request, 'doctor_profile/index.html')
