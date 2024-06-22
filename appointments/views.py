from django.shortcuts import render

# Create your views
from django.shortcuts import render


def index(request):
    return render(request, 'appointments/index.html')

# appointments/views.py

# appointments/views.py

from django.shortcuts import render
from .models import Doctor

def search(request):
    doctor_name = request.GET.get('doctor_name')
    specialization = request.GET.get('specialization')
    hospital = request.GET.get('hospital')
    date = request.GET.get('date')

    doctors = Doctor.objects.all()

    if doctor_name:
        doctors = doctors.filter(name__icontains=doctor_name)
    if specialization:
        doctors = doctors.filter(specialization__name__iexact=specialization)
    if hospital:
        doctors = doctors.filter(hospital__name__iexact=hospital)
    if date:
        doctors = doctors.filter(available_date=date)

    message = ""
    if doctors.exists():
        message = "Appointment is available. Sign in for proceeding with booking appointments."
        message_class = "alert-success"
    else:
        message = "No appointments available matching your criteria."
        message_class = "alert-danger"

    return render(request, 'appointments/search_results.html',
                  {'doctors': doctors, 'message': message, 'message_class': message_class})

