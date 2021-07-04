from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Member: #Member 라는 클라스 형성
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
def index(request):
    
    context = { #딕셔너리를 생성해서, 채워진 데이터를 render함수에 3번째 인자로 대입을 해주는 것이다    
        'post': { #post 라는 key는 딕셔너리 형태로 구성
            'author': 'Camilla',
            'body': 'My First Django Project'
        },
        'numbers': [10, 20, 30], #numbers의 key는 리스트로 구성
        'member': Member('Camilla', 30) #member라는 key는 클라스로

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