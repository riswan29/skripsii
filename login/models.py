from django.db import models
from django.contrib.auth.models import User

class Registrasi(models.Model):
    ROLE_CHOICES = (
        ('dosen','Dosen'),
        ('admin', 'Admin'),
        ('mahasiswa', 'Mahasiswa'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nim = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    username = models.CharField(max_length=100)
