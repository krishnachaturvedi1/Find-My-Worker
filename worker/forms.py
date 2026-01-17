from django import forms
from .models import Worker
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required', required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class WorkerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name','work_type', 'city', 'landmark', 'pin_code', 'contact_number', 'experience', 'availability', 'job_description', 'photo']

class WorkerLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label=("Password"), strip=False, widget=forms.PasswordInput)
    