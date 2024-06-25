from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

#def user_profile(request):
    #return render(request, 'user_profile/index.html')

from django.contrib.auth.decorators import login_required
from register.models import New

@login_required
def user_profile(request):
    newuser = New.objects.get(user=request.user)
    return render(request, 'user_profile/index.html', {
        'full_name': newuser.full_name,
        'email': request.user.email,
        'phone': newuser.phone,
        'nic': newuser.nic,
        'dob': newuser.dob,
    })
