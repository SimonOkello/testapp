from django.urls import path

from .views import (
    QuizListView,
    quizDetail,
    quiz_data_view,
    save_quiz_view
)
app_name = 'quizes'
urlpatterns = [
    path('', QuizListView.as_view(), name='quiz-list'),
    path('<quiz_id>/', quizDetail, name='quiz-detail'),
    path('<quiz_id>/data/', quiz_data_view, name='quiz-data-view'),
    path('<quiz_id>/save/', save_quiz_view, name='save-quiz-view'),
]
