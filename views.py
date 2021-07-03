from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    print('This is a post/ URL 패턴입니다') #로그로 남길수 있게 print, 
    return HttpResponse('Hello Camilla!')

def camilla(request):
    return HttpResponse('Hello Camilla Kim!')

def landingpage(request):
    return HttpResponse('This is a landing page')

def detail(request):
    return HttpResponse('This is a detail page')

def comments(request):
    return HttpResponse('This is a comments page')