from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dermatology, name='Dermatology'),
]