from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

#def doctor_profile(request):
    #return render(request, 'doctor_profile/index.html')

# views.py
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Doctor, Specialization

def doctor_list(request):
    specialization_name = request.GET.get('specialization')
    if specialization_name:
        doctors = Doctor.objects.filter(specialization__name=specialization_name)
        specialization = get_object_or_404(Specialization, name=specialization_name)
    else:
        doctors = Doctor.objects.all()
        specialization = None
    return render(request, 'doctor_profile/doctor_list.html', {'doctors': doctors, 'specialization': specialization})


def doctor_profile(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'doctor_profile/index.html', {'doctor': doctor})
