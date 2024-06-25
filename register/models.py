from django.db import models
from django.contrib.auth.models import User

class New(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    nic = models.CharField(max_length=12, unique=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])

    def __str__(self):
        return self.user.username

