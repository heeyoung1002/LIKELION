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
from django.urls import path
from posts import views

# server가 serving 가능한 URL 이 나와있는 모듈이다

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.index),
    path('camilla/', views.camilla),
    path('', views.landingpage),   #landing page등록을 위한 url 등록
]
