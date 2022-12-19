from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Quizserializer, RandomQuestionSerializer, AllQuestionsSerializer
from .models import Quizzes, Question


class Quiz(generics.ListAPIView):
    
    serializer_class = Quizserializer
    queryset = Quizzes.objects.all()



class RandomQuestion(APIView):
    
    def get(self, request, format=None, **kwargs):
        questions = Question.objects.filter(quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(questions, many=True)
        return Response(serializer.data)


class AllQuestions(APIView):
    
    def get(self, request, format=None, **kwargs):
        questions = Question.objects.filter(quiz__title=kwargs['topic'])
        serializer = AllQuestionsSerializer(questions, many=True)
        return Response(serializer.data)