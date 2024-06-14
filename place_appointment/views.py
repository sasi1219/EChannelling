from django.shortcuts import render

def place_appointment(request):
    return render(request, 'place_appointment/place_appointment.html')

