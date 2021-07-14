# post app 과 관련된 url 패턴을 post app 내부에서 독자적인 파일로 관리할 것인데

from django.urls import path
from . import views  #현재 디렉토리 (.) 에있는 같은 선상에 있는 views를 가져올래

app_name = 'posts'

urlpatterns = [
    path('', views.index, name= 'index'),
    path('<int:post_id>/', views.detail, name= 'detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    # /post/post_id로 받았을때의 url 패턴
]