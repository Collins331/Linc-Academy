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
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('team/', views.team, name='team'),
    path('testimonials/', views.testimonial, name='testimonial'),
    path('not_found/', views.not_found, name='not_found'),
    path('user/', views.user, name='user'),
]