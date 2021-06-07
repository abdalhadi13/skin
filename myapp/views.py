from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def testfun(request):
    return HttpResponse('Heyy')
def justfun(request):
    return HttpResponse('How are you')
def havefun(request):
    return render(request,'index.html')