"""mangostagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #include 함수를 추가로 import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')), #posts/ 라는 pattern으로 요청이 들어오면, 여기서 직접 view함수를 지정해주는게 아니라 include 함수를 사용해서 post 패키지 내부에 있는 url모듈을 참고해                
]
