from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

#def user_profile(request):
    #return render(request, 'user_profile/index.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def user_profile(request):
    # Assuming you have a User model with required fields like full_name, email, etc.
    user = request.user  # This gives you the current authenticated user

    # Pass user information to the template
    context = {
        'full_name': user.full_name,
        'email': user.email,
        'phone': user.phone,
        'nic': user.nic,
        'dob': user.dob,
        # Add more fields as needed
    }

    return render(request, 'user_profile/index.html', context)
