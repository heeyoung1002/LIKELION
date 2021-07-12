# post app 과 관련된 url 패턴을 post app 내부에서 독자적인 파일로 관리할 것인데

from django.urls import path
from . import views  #현재 디렉토리 (.) 에있는 같은 선상에 있는 views를 가져올래


urlpatterns = [
    path('', views.index),
    path('<int:post_id>/', views.detail),
    path('<int:post_id>/comments/', views.comments)
]