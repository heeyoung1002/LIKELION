from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('books/', views.index_books, name='booksindex'),
    path('books/<int:book_id>/', views.index_books_detail, name='bookdetail'),
    path('videos/', views.index_videos, name='videosindex'),
    path('videos/<int:video_id>/', views.index_videos_detail, name='videodetail'),
    path('websites/', views.index_websites, name='websitesindex'),
    path('websites/<int:video_id>/', views.index_websites_detail, name='websitedetail'),
] 