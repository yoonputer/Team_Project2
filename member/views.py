from django.shortcuts import render

# Create your views here.


def memberview(request):
    return render(request, 'member/member.html')
