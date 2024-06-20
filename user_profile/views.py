from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def user_profile(request):
    return render(request, 'user_profile/index.html')
