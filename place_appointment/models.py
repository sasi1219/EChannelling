from django.db import models
from doctor_profile.models import Doctor, Hospital
from register.models import New

class Appointment(models.Model):
    reference_number = models.CharField(max_length=10)
    appointment_number = models.IntegerField()
    patient = models.ForeignKey(New, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Appointment {self.appointment_number} for {self.patient.full_name} with Dr. {self.doctor.name} on {self.appointment_date}"

