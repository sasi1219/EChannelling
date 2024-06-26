from django.shortcuts import render

# Create your views
from django.shortcuts import render


def index(request):
    return render(request, 'appointments/index.html')

from django.shortcuts import render
from .models import Check

def search(request):
    doctor_name = request.GET.get('doctor_name')
    specialization = request.GET.get('specialization')
    hospital = request.GET.get('hospital')
    date = request.GET.get('date')

    checks = Check.objects.all()

    if doctor_name:
        checks = checks.filter(name__name__icontains=doctor_name)
    if specialization:
        checks = checks.filter(specialization__name__iexact=specialization)
    if hospital:
        checks = checks.filter(hospital__name__iexact=hospital)
    if date:
        checks = checks.filter(available_date=date)

    message = ""
    if checks.exists():
        message = "Appointment is available. Sign in for proceeding with booking appointments."
        message_class = "alert-success"
    else:
        message = "No appointments available matching your criteria."
        message_class = "alert-danger"

    return render(request, 'appointments/search_results.html',
                  {'checks': checks, 'message': message, 'message_class': message_class})



