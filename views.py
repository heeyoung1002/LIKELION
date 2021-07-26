from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Members

def index(request):
    return render (request, 'login/index.html')

# member 함수가 실제로 호출 될 때에는 request라는 파라미터에 HTTP관련한 모든 정보가 담긴다
def member(request):
    # GET 방식으로 호출된 모든 데이터를 받을 수 있다
    ID = request.POST.get('ID')
    PW = request.POST.get('PW')

    # ID,PW 를 사용해서 새로운 게시물을 생성한다
    # 헤딩 인스턴스를 만들어서 인스턴스를 변수에 저장
    member = Members(username=ID, password=PW)
    member.save()

    return redirect('mainpage:mainpageindex')
