from django.shortcuts import render

from django.shortcuts import render

def signin(request):
    return render(request, 'signin/signin.html')

