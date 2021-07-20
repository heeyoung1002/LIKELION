from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index_books(request):
    context = {
        'post' : {
            'title': 'book title',
            'image': 'book image',
        }
    }
    return render (request, 'library/index.html', context)

def index_videos(request):
    return render (request, 'library/index.html')

def index_websites(request):
    return render (request, 'library/index.html')