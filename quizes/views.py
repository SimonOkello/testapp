from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.http import JsonResponse
# Create your views here.
from . models import Quiz
from questions.models import Question


class QuizListView(ListView):
    model = Quiz
    template_name = 'quizes/home.html'


def quizDetail(request, quiz_id):
    obj = get_object_or_404(Quiz, pk=quiz_id)
    return render(request, 'quizes/quiz-detail.html', {'obj': obj})


def quiz_data_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = []
    for question in quiz.get_questions():
        answers = []
        for answer in question.get_answers():
            answers.append(answer.name)
        questions.append({str(question): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time_to_complete
    })


def save_quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    user = request.user
    if request.is_ajax():
        print(request.POST)
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')
        print('DATA:', data_)
        for k in data_.keys():
            print('Key: ', k)
            question = Question.objects.get(name=k)
            questions.append(question)
        print("Questions:", questions)
        score = 0
        multiplier = 100/quiz.number_of_questions
        results = []
        correct = None

        for question in questions:
            ans_selected = request.POST.get(question.name)
            print("Selected: ", ans_selected)
    return JsonResponse({'text': 'works'})
