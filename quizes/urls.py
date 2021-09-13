from django.urls import path

from .views import (
    QuizListView,
    quizDetail
)
app_name = 'quizes'
urlpatterns = [
    path('', QuizListView.as_view(), name='quiz-list'),
    path('<quiz_id>', quizDetail, name='quiz-detail'),
]
