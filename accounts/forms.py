from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegisterForm(UserCreationForm):
    # UserCreationForm already username + password + confirm password deta hai
    # Hum bas email, phone, role add kar rahe hain

    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    role = forms.ChoiceField(choices=User.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'role', 'password1', 'password2']
