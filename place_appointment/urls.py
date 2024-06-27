
from django.urls import path
from . import views

urlpatterns = [
    path('', views.find_doctor, name='find_doctor'),
    path('check_doctor', views.check_doctor, name='check_doctor'),
]


