from django.shortcuts import render

# Create your views here.
def dashboardMHS(request):
    return render(request, 'mahasiswa/index.html')
