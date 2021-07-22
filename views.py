from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Video, Website


# Create your views here.

def index_books(request):
    books = Book.objects.all() #Book 이라는 테이블에 저장되어있는 모든 파일을 불러와서 books라는 변수에 저장한다
    
    context = {
        'books' : books,
        'levels' : ['AR 0.1 - 0.9대', 'AR 1.0 - 1.9대', 'AR 2.0 - 2.9대', 'AR 3.0 - 3.9대', 'AR 4.0 - 4.9대', 'AR 5.0 - 5.9대'],
    }
    return render (request, 'library/index_book.html', context)


def index_videos(request):
    videos = Video.objects.all() #Video 이라는 테이블에 저장되어있는 모든 파일을 불러와서 videos라는 변수에 저장한다 

    context = {
        'videos' : videos,
        'levels' : ['미취학 아동', '초등 저학년 추천영상', '초등 고학년 추천영상']
    }
    return render (request, 'library/index_video.html')


def index_websites(request):

    return render (request, 'library/index_library.html')