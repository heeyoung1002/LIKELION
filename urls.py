from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', include('books.urls')),
    path('videos/', include('videos.urls')),
    path('websites/', include('websites.urls')),
    path('login/', include('login.urls')),
]