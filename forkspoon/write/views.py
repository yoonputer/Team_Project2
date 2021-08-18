from django.shortcuts import render, redirect
from Spredict import Spredict  # 딥러닝 파일
from wordc import mkwdcrd  # 딥러닝 파일


def writeview(request):
    if request.method == 'POST':
        contents = request.POST['contents']
        myemail = request.POST['emailtab']
        predict_content = Spredict()
        result = predict_content.sentance_predict(contents)
        # 사이트에서 나의 자소서를 가져옴
        context = {'score': str(result[1])+"점", 'myemail': 'write/'+myemail+'.png'}
        mkwdcrd(contents, myemail)
        return render(request, 'write/result.html', context)
    else:
        return render(request, 'write/write.html')
