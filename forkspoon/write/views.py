from django.shortcuts import render

# Create your views here.


def writeview(request):
    return render(request, 'write/write.html')
