from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),  # URL for the sign-in page

    # Other URLs...
]
