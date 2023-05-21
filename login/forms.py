from .models import Registrasi
from django import forms
from django.contrib.auth.models import User

class RegistrasiForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    konfirmasi_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Registrasi
        fields = ['nim', 'username', 'password', 'konfirmasi_password', 'role']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        konfirmasi_password = cleaned_data.get('konfirmasi_password')

        if password and konfirmasi_password and password != konfirmasi_password:
            raise forms.ValidationError("Password dan konfirmasi password tidak cocok")
