from django.shortcuts import render

# Create your views here.

def dashboardDSN(request):
    return render(request, 'dosen/index.html')
