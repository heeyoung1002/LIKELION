from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.index_books, name='booksindex'),
    path('videos/', views.index_videos, name='videosindex'),
    path('websites/', views.index_websites, name='websitesindex'),
    path('books/<int:book_id>/', views.index_books_detail)
] 