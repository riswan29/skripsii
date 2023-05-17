from django.contrib import admin
from django.urls import path
from app.views import *
from login.views import *
from mahasiswa.views import *
from dosen.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DISKUSI, name='diskusi'),
    path('login', login, name='login'),
    path('dosen', l_dosen, name='login_dosen'),
    path('mahasiswa', l_mahasiswa, name='login_mahasiswa'),
    path('mahasiswa/dashboard', dashboardMHS, name='dashboardMHS'),
    path('dosen/dashboard', dashboardDSN, name='dashboardDSN'),
]
