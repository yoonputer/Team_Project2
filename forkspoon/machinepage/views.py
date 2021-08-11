from django.shortcuts import render

# Create your views here.

def machineview(request):
    return render(request, 'machinepage/machinepage.html')