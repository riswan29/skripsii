from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from login.models import Pengguna

def registrasi(request):
    if request.method == 'POST':
        username = request.POST['username']
        nim = request.POST['nim']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        role = request.POST['role']

        if password == confirm_password:
            pengguna = Pengguna(username=username, nim=nim, password=password, role=role)
            pengguna.save()
            return redirect('login')
        else:
            error_message = 'Password dan konfirmasi password tidak cocok.'
            return render(request, 'registrasi.html', {'error_message': error_message})

    return render(request, 'registrasi.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Pengguna berhasil masuk atau terotentikasi
            login(request, user)  # Melakukan login dengan user yang valid
            print("Username:", user.username)
            print("Role:", user.role)

            # Periksa peran (role) pengguna
            if user.role == 'dosen':
                return redirect('dosen_dashboard')  # Redirect ke halaman dosen
            else:
                return redirect('mahasiswa_dashboard')  # Redirect ke halaman mahasiswa
        else:
            # Pengguna gagal masuk atau otentikasi
            return redirect('dashboard')  # Redirect kembali ke halaman login jika gagal
    else:
        # Akses GET ke halaman login
        return render(request, 'login.html')

def dashboardMHS(request):
    # Mengambil semua pengguna dengan role mahasiswa dari database
    mahasiswa_list = Pengguna.objects.filter(role='mahasiswa')
    print(mahasiswa_list)
    context = {'mahasiswa_list': mahasiswa_list}
    return render(request, 'mahasiswa/index.html', context)
def dashboardDSN(request):
    # Mengambil semua pengguna dengan role dosen dari database
    dosen_list = Pengguna.objects.filter(role='dosen')
    context = {'dosen_list': dosen_list}
    return render(request, 'dosen/index.html', context)
