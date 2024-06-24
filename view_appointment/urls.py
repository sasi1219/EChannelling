from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_appointment, name='view_appointment'),
]