from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index_books(request):
    return render (request, 'library/index.html')

def index_videos(request):
    return HttpResponse('This is Video page')

def index_websites(request):
    return HttpResponse('This is Website page')