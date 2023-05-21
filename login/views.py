from django.shortcuts import render, redirect
from .forms import RegistrasiForm
from django.contrib.auth.models import User
from django.db import IntegrityError

def registrasi(request):
    if request.method == 'POST':
        form = RegistrasiForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['nim']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            try:
                # Buat pengguna baru
                user = User.objects.create_user(username=username, password=password)
                user.save()

                # Simpan data registrasi
                registrasi = form.save(commit=False)
                registrasi.user = user
                registrasi.save()

                return redirect('success')

            except IntegrityError:
                form.add_error('nim', 'NIM sudah terdaftar.')
    else:
        form = RegistrasiForm()

    context = {'form': form}
    return render(request, 'registrasi.html', context)

def success(request):
    return render(request, 'success.html')
