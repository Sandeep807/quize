
from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import serializer_helpers
from .models import *
from django.contrib.auth.models import User

class BaseSerializer(serializers.Serializer):
    first_name=serializers.CharField(required=True)
    mobilenumber=serializers.CharField(required=True)
    password=serializers.CharField(required=True)
    confirm_passwrod=serializers.CharField(required=True)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['category_name']
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answerss
        fields=['answer']
class QusetionSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    answers=AnswerSerializer(read_only=True,many=True)
    
    class Meta:
        model=Question
        #fields=['category','answers']
        fields=['uid','question','category','answers']
# class QuizRedySerializer(serializers.ModelSerializer):
#     class Meta:
#         model=QuizRedy

class AnswerSerializer(serializers.ModelSerializer):
    question=QusetionSerializer()
    class Meta:
        model=Answerss
        fields=['answer','question']
class SimpleSerializer(serializers.Serializer):
    user_id=serializers.IntegerField(required=True)
    question_id=serializers.UUIDField(required=True)
    answer=serializers.CharField(required=True)

class SimpleQuizSerializer(serializers.Serializer):
    category_name=serializers.CharField(required=True)
    question_limit=serializers.IntegerField(required=True)
class StoreQuizSerializer(serializers.ModelSerializer):
    question=AnswerSerializer()
    class Meta:
        model=StoreQuiz
        fields=['totalmarks','question']


class UserSerializer(serializers.ModelSerializer):
    storequiz=StoreQuizSerializer(read_only=True,many=True)
    class Meta:
        model=User
        fields=['username','email','storequiz']

# from django.db.models import fields
# from rest_framework import serializers
# from rest_framework.views import exception_handler
# from .models import *

# class QuestionSerializer(serializers.ModelSerializer):
#     answers  = serializers.SerializerMethodField()
#     class Meta:
#         model = Question
#         exclude = ['created_at' , 'updated_at' , 'category']
    
#     def get_answers(self , obj):
#         serializer = AnswerSerializer(obj.answer.all() , many = True)
#         return serializer.data


# class AnswerSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Answer
#         exclude = ['created_at' , 'updated_at' , 'uid' , 'is_correct' , 'question']


# class QuizSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Quiz
#         exclude = ['created_at' , 'updated_at']


# class QuizQuestionsSerializer(serializers.ModelSerializer):
#     questions = serializers.SerializerMethodField()
#     class Meta:
#         model = QuizQuestions
#         exclude = ['created_at' , 'updated_at' , 'uid' , 'quiz']


#     def get_questions(self , obj):
#         serializer = QuestionSerializer(obj.question)
#         return serializer.data


# class CheckQuestionSerializer(serializers.Serializer):
#     answer = serializers.CharField()
#     question = serializers.UUIDField()