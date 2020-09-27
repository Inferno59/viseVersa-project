from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def reverseStr(request):

    originStr = request.GET['usertext']
    reversedStr = reversed(originStr)
    countOriginWords = len(originStr.split())

    context = {
        "originStr": originStr,
        "reversedStr": reversedStr,
        "countOriginWords": countOriginWords
    }
    return render(request, 'reversed.html', context)
