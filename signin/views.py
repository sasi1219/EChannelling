from django.middleware.csrf import get_token
from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirect to user profile after successful login
            return redirect('user_profile')
        else:
            # Handle invalid login
            # You might want to add an error message here

            context = {'csrf_token': get_token(request),
                       'error': 'Invalid username or password'}
            return render(request, 'signin/signin.html', context)

    return render(request, 'signin/signin.html')

