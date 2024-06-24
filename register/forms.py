from django import forms
from .models import RegUser

class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
      Feature-Register_page
        model = RegUser

        
        main
        fields = ['full_name', 'email', 'username', 'password', 'confirm_password', 'nic', 'phone', 'dob', 'gender', 'terms_agreed']
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
