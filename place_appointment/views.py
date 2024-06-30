import random
from appointments.models import Check
from datetime import datetime
from django.shortcuts import render, redirect
from .models import Appointment
from doctor_profile.models import Doctor, Hospital
from register.models import New

def find_doctor(request):
    return render(request, 'place_appointment/Find_doctor.html')

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

    if checks.exists():
        check = checks.first()

        # Generate reference number and appointment number
        reference_number = str(random.randint(100000, 999999))
        appointment_number = Appointment.objects.filter(
            doctor=check.name,
            hospital=check.hospital,
            appointment_date=check.available_date
        ).count() + 1

        return render(request, 'place_appointment/book_appointment.html', {
            'check': check,
            'reference_number': reference_number,
            'appointment_number': appointment_number,
            'appointment_date': check.available_date,
            'message': "Appointment is available. Book your Appointment.",
            'message_class': "alert-success"
        })

    else:
        return render(request, 'place_appointment/Find_doctor.html', {
            'message': "No appointments available matching your criteria.",
            'message_class': "alert-danger"
        })



def book_appointment(request):
    if request.method == "POST":
        doctor_id = request.POST.get('doctor_id')
        hospital_id = request.POST.get('hospital_id')
        appointment_date = request.POST.get('appointment_date')
        reference_number = request.POST.get('reference_number')
        appointment_number = request.POST.get('appointment_number')

        appointment_date = datetime.strptime(appointment_date, "%B %d, %Y").strftime('%Y-%m-%d')

        # Retrieve objects from IDs
        doctor = Doctor.objects.get(id=doctor_id)
        hospital = Hospital.objects.get(id=hospital_id)
        patient = New.objects.get(user=request.user)  # Assuming New has a user field

        # Create Appointment object
        appointment = Appointment.objects.create(
            reference_number=reference_number,
            appointment_number=appointment_number,
            patient=patient,
            doctor=doctor,
            hospital=hospital,
            appointment_date=appointment_date,
            fee=doctor.fee
        )

        # Render success template with necessary context
        return render(request, 'place_appointment/book_success.html', {
            'appointment': appointment  # Pass any data you want to display on success
        })

    # Redirect to find_doctor page if not a POST request
    return redirect('find_doctor')
