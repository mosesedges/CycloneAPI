from .models import Question, Quizzes, Answer
from  rest_framework import serializers

class Quizserializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quizzes
        fields = [
            'title', 
            'category',
            'date_created',
        ]

class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Answer
        fields =[
            'id',
            'answer_text',
            'is_right'
        ]
        
class RandomQuestionSerializer(serializers.ModelSerializer):
    
    answer = AnswerSerializer(many=True, read_only=True)
    quiz = Quizserializer(read_only=True)
    
    class Meta:
        model = Question
        fields =[
            'title',
            'answer',
            'quiz',
            
        ]
        
class AllQuestionsSerializer(serializers.ModelSerializer):
    
    answer = AnswerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields =[
            'title',
            'difficulty',
            'answer',
            
        ]