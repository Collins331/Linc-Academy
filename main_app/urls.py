from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.quiz, name='quiz'),
    path('addquiz/', views.addquiz, name='addquiz'),
    path('postquiz', views.postquiz, name='postquiz'),
]