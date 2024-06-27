from django.shortcuts import render

def find_doctor(request):
    return render(request, 'place_appointment/Find_doctor.html')

from django.shortcuts import render
from appointments.models import Check

def check_doctor(request):
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
        message = "Appointment is available. Book your Appointment."
        message_class = "alert-success"
        return render(request, 'place_appointment/book_appointment.html',
                      {'checks': checks, 'message': message, 'message_class': message_class})
    else:
        message = "No appointments available matching your criteria."
        message_class = "alert-danger"
        return render(request, 'place_appointment/find_doctor.html',
                      {'message': message, 'message_class': message_class})
