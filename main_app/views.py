from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/index.html')


def quiz(request):
    return render(request, 'quiz.html')

def addquiz(request):
    return render(request, 'add_quiz.html')
