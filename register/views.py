from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            return redirect('success')
        else:
            messages.error(request, 'Please correct the errors.')
    else:
        form = UserRegistrationForm()
    return render(request, 'register/index.html', {'form': form})

def success(request):
    return render(request, 'register/success.html')
