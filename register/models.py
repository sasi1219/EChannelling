from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=100)
    nic = models.CharField(max_length=12, unique=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    terms_agreed = models.BooleanField(default=False)
