from django.urls import path
from .views import Quiz, RandomQuestion, AllQuestions

app_name = 'quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('random/<str:topic>/', RandomQuestion.as_view(), name='random'),
    path('all/<str:topic>/', AllQuestions.as_view(), name='questions'),
]

