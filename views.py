from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.\

def index(request):
    #post table에 저장되어있는 모든 데이터를 posts 라는 변수에 저장한다
    posts = Post.objects.all().order_by('created_at')

    context = { # 게시물 딕셔너리를 여러개 담고 있는 리스트
        'posts' : posts
    }

    return render(request, 'posts/index.html', context)
    # context라는 복합적인 데이터를 담고있는 데이터를 post/index.html이라는 template 에 전달해주면
    # index.html 파일에서는 context라는 딕셔너리에 있는 데이터를 
    # post, numbers, memebers (key값)를 변수로 받아서 사용한다

def camilla(request):
    return HttpResponse('Hello Camilla Kim!')

def landingpage(request):
    return HttpResponse('This is a landing page')

def detail(request, post_id):
    return HttpResponse(f'Post {post_id} Detail')

def comments(request, post_id):
    return HttpResponse(f'Post {post_id} Comments')