# models.py
from django.db import models

class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    experience_years = models.IntegerField()
    qualification = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    available_days = models.CharField(max_length=100)
    image = models.ImageField(upload_to='doctor_profile/static/images', null=True, blank=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
