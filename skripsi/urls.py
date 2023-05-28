from django.contrib import admin
from django.urls import path
from app.views import *
from mahasiswa.views import *
from dosen.views import *
from login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DISKUSI, name='diskusi'),
    path('registration/', registration_view, name='registration'),
    path('success/', success_view, name='success'),
    path('new-chat/', newChat, name='newChat'),
    path('chat/<str:search>/', loadChat, name='loadChat'),
]
