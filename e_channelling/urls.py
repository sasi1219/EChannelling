"""
URL configuration for e_channelling project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appointments.urls')),
    path('register/', include('register.urls')),
    path('login/', include('signin.urls')),
    path('appointments/', include('place_appointment.urls')),
    path('profile/', include('user_profile.urls')),
    path('privacy_policy/', include('privacy_policy.urls')),
    path('terms_and_conditions/', include('terms_and_conditions.urls')),
    path('aboutus/', include('about_us.urls')),
    path('search/', include('appointments.urls')),
    path('Cardiology/', include('Cardiology.urls')),
    path('success/', include('register.urls')),
    path('Dermatology/', include('Dermatology.urls')),
]