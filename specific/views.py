from django.shortcuts import render


# Create your views here.

def kalayan(request):
    return render(request,'kalayan.html')


def nvn(request):
    return render(request,'nvn.html')
