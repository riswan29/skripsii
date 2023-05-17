from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def l_dosen(request):
    return render(request, 'dosen/login_dosen.html')

def l_mahasiswa(request):
    return render(request, 'mahasiswa/login_mahasiswa.html')
