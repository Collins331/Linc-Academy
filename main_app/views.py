from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Quize

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, 'main/index.html')


@login_required(login_url='login')
def quiz(request):
    return render(request, 'quiz.html')


@login_required(login_url='login')
def addquiz(request):
    return render(request, 'add_quiz.html')




def postquiz(request):
    if request.method == 'POST':
        question = request.POST['quiz']
        option1 = request.POST['option1']
        option2 = request.POST['option2']
        option3 = request.POST['option3']
        option4 = request.POST['option4']
        answer = request.POST['answer']
        author = request.POST['author']
        quiz = Quize(question=question, option1=option1, option2=option2, option3=option3, option4=option4, answer=answer, author=author)
        quiz.save()
        return redirect("/addquiz")
    return redirect("/quiz")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('user')

def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')


def courses(request):
    return render(request, 'main/courses.html')

def testimonial(request):
    return render(request, 'main/testimonial.html')

def team(request):
    return render(request, 'main/team.html')

def not_found(request):
    return render(request, '404.html')


def user(request):
    return render(request, 'user/user.html')