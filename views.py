from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Video, Website
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse


def index_books(request):
    
    # Book 이라는 테이블에 저장되어있는 모든 파일을 불러와서 books라는 변수에 저장한다
    books = Book.objects.all().order_by('level')
    
    # 레벨 별 리스트 생성
    book1 = []
    book2 = []
    book3 = []
    book4 = []
    book5 = []
    book6 = []

    # book 정보중 level을 필터링 하기 위해 for 문으로 반복
    # 모델에서 지정해준 형식으로 반환하는 book[0]의 데이터
    # 0.8 : Biscuit 시리즈 'Biscuit Finds a Friend' : Alyssa Satin Capucilli
    # '{self.level} : {self.title} : {self.author}
    
    for i in books : 
        book_str = str(i)
        book_float = float (book_str[0:3])

        if book_float >= 0.1 and book_float < 1.0 : # 변환 된 book_float 를 비교 
            book1.append(i)
        elif book_float >= 1.0 and book_float < 2.0 :
            book2.append(i)
        elif book_float >= 2.0 and book_float <3.0 :
            book3.append(i)
        elif book_float >= 3.0 and book_float <4.0 :
            book4.append(i)
        elif book_float >=4.0 and book_float <5.0 :
            book5.append(i)
        elif book_float >=5.0 and book_float <6.0 :
            book6.append (i)
    
    context = {
        # 'books' : books,
        'book1' : book1,
        'book2' : book2,
        'book3' : book3,
        'book4' : book4,
        'book5' : book5,
        'book6' : book6,

        'levels' : ['AR 0.1 - 0.9', 'AR 1.0 - 1.9', 'AR 2.0 - 2.9', 'AR 3.0 - 3.9', 'AR 4.0 - 4.9', 'AR 5.0 - 5.9'],
    }

    return render (request, 'library/index_book.html', context)

def index_books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {'book' : book}
    return render (request, 'library/index_book_detail.html', context)


@login_required
def booklike(request, book_id):
    if request.method == 'POST':

        try:
            book = Book.objects.get(id=book_id)

            if request.user in book.liked_users.all():
                book.liked_users.remove(request.user)
            else:
                book.liked_users.add(request.user)
        
            return HttpResponseRedirect(reverse('library:bookdetail', kwargs={'book_id':book.id}))
    
        except Book.DoesNotExist:
            pass

    return redirect('library:booksindex')






def index_videos(request):
    videos = Video.objects.all() #Video 이라는 테이블에 저장되어있는 모든 파일을 불러와서 videos라는 변수에 저장한다 
    
    # 레벨 별 리스트 생성
    video1 = []
    video2 = []
    video3 = []
    
    for i in videos : 
        video_str = str(i) #앞 3글자를 0.8을 자르기 위해 문자열로 변환
        video_float = float (video_str[0:3]) #문자열로 변환 후 맨 앞 0.8 만 자르기 함수 사용 #값 비교를 위해 float 형식으로 변환

        if video_float == 1.0 : # 변환 된 book_float 를 비교 
            video1.append(i)
        elif video_float == 2.0 :
            video2.append(i)
        elif video_float == 3.0 :
            video3.append(i)
    
    context = {
        # 'videos' : videos,
        'video1' : video1,
        'video2' : video2,
        'video3' : video3,
        
        'levels' : ['미취학 아동 추천 채널', '초등 저학년 추천 채널', '초등 고학년 추천 채널']
    }
    return render (request, 'library/index_video.html', context)


def index_videos_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    context = {'video' : video}
    return render (request, 'library/index_video_detail.html', context)


@login_required
def videolike(request, video_id):
    if request.method == 'POST':

        try:
            video = Video.objects.get(id=video_id)

            if request.user in video.liked_users.all():
                video.liked_users.remove(request.user)
            else:
                video.liked_users.add(request.user)
        
            return HttpResponseRedirect(reverse('library:videodetail', kwargs={'video_id':video.id}))
    
        except Video.DoesNotExist:
            pass

    return redirect('library:videosindex')






def index_websites(request):
    websites = Website.objects.all() #Video 이라는 테이블에 저장되어있는 모든 파일을 불러와서 videos라는 변수에 저장한다 

    # 웹사이트별 리스트 생성
    website1 = []
    website2 = []
    website3 = []
    
    for i in websites : 
        website_str = str(i) #앞 3글자를 0.8을 자르기 위해 문자열로 변환
        website_float = float (website_str[0:3]) #문자열로 변환 후 맨 앞 0.8 만 자르기 함수 사용 #값 비교를 위해 float 형식으로 변환

        if website_float == 1.0 : # 변환 된 website_float 를 비교 
            website1.append(i)
        elif website_float == 2.0 :
            website2.append(i)
        elif website_float == 3.0 :
            website3.append(i)
    
    context = {
        # 'websites' : websites,
        'website1' : website1,
        'website2' : website2,
        'website3' : website3,
        
        'levels' : ['엄빠표 영어도서', '웹사이트 (무료)', '웹사이트 (유료)']
    }
    return render (request, 'library/index_website.html', context)


def index_websites_detail(request, website_id):
    website = Website.objects.get(id=website_id)
    context = {'website' : website}
    return render (request, 'library/index_website_detail.html', context)



@login_required
def websitelike(request, website_id):
    if request.method == 'POST':

        try:
            website = Website.objects.get(id=website_id)

            if request.user in website.liked_users.all():
                website.liked_users.remove(request.user)
            else:
                website.liked_users.add(request.user)
        
            return HttpResponseRedirect(reverse('library:websitedetail', kwargs={'website_id':website.id}))
    
        except Website.DoesNotExist:
            pass

    return redirect('library:websitesindex')