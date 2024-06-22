from django.urls import path
from . import views

urlpatterns = [
    path('', views.Cardiology, name='Cardiology'),
]