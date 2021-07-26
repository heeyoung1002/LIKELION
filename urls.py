from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.index, name='loginindex'),
    path('member/', views.member, name='member'),
    # path('signup/', views.signup, name='signup'),
    # path('logout/', views.logout, name='logout'),
]