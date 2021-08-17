from django.shortcuts import render

# Create your views here.


def trendview(request):
    return render(request, 'trend/trend.html')


