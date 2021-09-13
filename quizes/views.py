from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
# Create your views here.
from . models import Quiz
class QuizListView(ListView):
    model=Quiz
    template_name ='quizes/home.html'


def quizDetail(request, quiz_id):
    obj = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quizes/quiz-detail.html', {'obj':obj})