from django.urls import path
from . import views

urlpatterns = [
    path('', views.place_appointment, name='place_appointment'),
]

