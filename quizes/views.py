from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.http import JsonResponse
# Create your views here.
from . models import Quiz
class QuizListView(ListView):
    model=Quiz
    template_name ='quizes/home.html'


def quizDetail(request, quiz_id):
    obj = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quizes/quiz-detail.html', {'obj':obj})


def quiz_data_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = []
    for question in quiz.get_questions():
        answers=[]
        for answer in question.get_answers():
            answers.append(answer.name)
        questions.append({str(question):answers})
    return JsonResponse({
        'data':questions,
        'time':quiz.time_to_complete
    })
