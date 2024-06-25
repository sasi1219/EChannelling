from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            return redirect('user_profile')
        else:
            return render(request, 'signin/signin.html', {'error': 'Invalid username or password'})
    return render(request, 'signin/signin.html')


