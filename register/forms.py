from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import New

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    full_name = forms.CharField(max_length=100)
    nic = forms.CharField(max_length=12)
    phone = forms.CharField(max_length=15)
    dob = forms.DateField()
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            newuser = New(
                user=user,
                full_name=self.cleaned_data['full_name'],
                nic=self.cleaned_data['nic'],
                phone=self.cleaned_data['phone'],
                dob=self.cleaned_data['dob'],
                gender=self.cleaned_data['gender'],

            )
            newuser.save()
        return user
