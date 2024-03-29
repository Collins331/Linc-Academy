from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('addquiz/', views.addquiz, name='addquiz'),
    path('postquiz', views.postquiz, name='postquiz'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
]