from django.shortcuts import render, redirect
from . models import Quize

# Create your views here.
def home(request):
    return render(request, 'main/index.html')


def quiz(request):
    return render(request, 'quiz.html')

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
