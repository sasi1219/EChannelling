from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Doctor, Specialization, Hospital

admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(Hospital)
