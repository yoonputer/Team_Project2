from django.shortcuts import render

# Create your views here.


def writeview(request):
    return render(request, 'write/write.html')


def result(request):
    return render(request, 'write/result.html')
