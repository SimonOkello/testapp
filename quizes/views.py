from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.http import JsonResponse
# Create your views here.
from . models import Quiz
from questions.models import Answer, Question
from results.models import Result


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
    if request.is_ajax():
        user = request.user
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            question = Question.objects.get(name=k)
            questions.append(question)
        score = 0
        multiplier = 100/quiz.number_of_questions
        results = []
        correct_answer = None
        for question in questions:
            selected_answer = request.POST.get(question.name)
            if selected_answer != "":
                question_answers = Answer.objects.filter(question=question)
                for answer in question_answers:
                    if selected_answer == answer.name:
                        if answer.correct:
                            score += 1
                            correct_answer = answer.name
                    else:
                        if answer.correct:
                            correct_answer = answer.name
                results.append(
                    {str(question): {'correct_answer': correct_answer, 'answered': selected_answer}})
            else:
                results.append({str(question): 'not answered'})

        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)
        if score_ >= quiz.pass_mark:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})
    return JsonResponse({'text': 'works'})
