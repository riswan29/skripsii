from django.contrib import admin
from django.urls import path
from app.views import *
from login.views import *
from mahasiswa.views import *
from dosen.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DISKUSI, name='diskusi'),
    path('login', user_login, name='login'),
    # path('dosen/dashboard/', dosen_dashboard, name='dosen_dashboard'),
    # path('mahasiswa/dashboard/', mahasiswa_dashboard, name='mahasiswa_dashboard'),
    # ...
    path('mahasiswa/dashboard/', dashboardMHS, name='dashboardMHS'),
    path('dosen/dashboard/', dashboardDSN, name='dashboardDSN'),
    path('admin/', admin.site.urls),
    path('registrasi/', registrasi, name='registrasi'),
]
