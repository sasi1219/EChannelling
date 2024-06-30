from django.shortcuts import render

from django.shortcuts import render
from place_appointment.models import Appointment
from django.contrib.auth.decorators import login_required


@login_required
def view_appointment(request):
    # Fetch the logged-in user's appointments
    user = request.user
    upcoming_appointments = Appointment.objects.filter(patient__user=user).order_by('appointment_date')

    context = {
        'upcoming_appointments': upcoming_appointments,
    }

    return render(request, 'view_appointment.html', context)
