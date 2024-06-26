from django.contrib import admin

# Register your models here.
# admin.py
# admin.py
from django.contrib import admin
from .models import Doctor, Specialization, Hospital

admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(Hospital)
