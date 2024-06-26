from django.db import models

# Create your models here.


from django.db import models
from doctor_profile.models import Doctor, Specialization, Hospital

class Check(models.Model):
    name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    available_date = models.DateField()

    def __str__(self):
        return f"Check: Dr. {self.name.name} - {self.specialization.name} at {self.hospital.name} on {self.available_date}"
