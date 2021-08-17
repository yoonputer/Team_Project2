from django.shortcuts import render, redirect

# Create your views here.


def writeview(request):
    if request.method == 'POST':
        contents = request.POST['contents']
        myemail = request.POST['emailtab']

        # 사이트에서 나의 자소서를 가져옴
        print(contents, myemail)
        return render(request, 'write/result.html')
    else:
        return render(request, 'write/write.html')
