
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializer import *

from .models import *
# Create your views here.
class UserView(APIView):
    def Post(self,request):
        try:
            data=request.data
            serializer=BaseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status':'Success',
                    'data':serializer.data
                })
            return Response({
                'status':'False',
                'message':serializer.errors
            })
        except Exception as e:
            return Response({
                'status':'False',
                'message':'somthing went wrong'
            })

class QuizRedyView(APIView):
    def get(self,request):
        try:
            data=request.data
            checkserializer=SimpleQuizSerializer(data=data)
            if checkserializer.is_valid():
                obj=Question.objects.filter(category__category_name=checkserializer.data['category_name'])[0:checkserializer.data['question_limit']]

                if len(obj)<0:
                    return Response({
                        'status':"False",
                        'message':'you have wrong fill category name'
                    })
                serializer=QusetionSerializer(obj,many=True)
                print(serializer)
                return Response({
                    'message':serializer.data
                })
            return Response({
                    'message':checkserializer.errors
                })
        except Exception as e:
            print(e)
            return Response({
                'message':'somthing went wrong'
            })
    def post(self,request):
        try:
            data=request.data
            serializer=SimpleSerializer(data=data)
            if serializer.is_valid():
                obj=Question.objects.filter(uid=serializer.data['question_id']).first()
                print(obj)
                if obj is None:
                    return Response({
                        'status':'False',
                        'message':'Question is not valid'
                    })

                if obj.answers.filter(answer=serializer.data['answer']).exists():

                    answer=obj.answers.filter(answer=serializer.data['answer'],is_correct=True).first()
                    user=User.objects.filter(id=serializer.data['user_id']).first()
                    if answer is not None:
                        user=User.objects.filter(id=serializer.data['user_id']).first()
                        store=StoreQuiz.objects.filter(user__id=serializer.data['user_id']).first()

                        if store is None:
                            StoreQuiz.objects.create(
                            totalmarks=2,
                            user=user,
                            question=answer,
                            youranswer=True
                            )
                            return Response({
                                    'status':'Success',
                                    'message':'Your answer is correct'
                                })
                        else:
                            StoreQuiz.objects.create(
                            totalmarks=2,
                            user=user,
                            question=answer,
                            youranswer=True
                            )
                            return Response({
                                    'status':'Success',
                                    'message':'Your answer is correct'
                                    })
                    else: 
                        StoreQuiz.objects.create(
                            totalmarks=-2,
                            user=user,
                            question=answer,
                            youranswer=True
                            )           
                        return Response({
                            'status':'False',
                            'message':'Your answer is not correct'
                        })
                return Response({
                    'status':'False',
                    'message':'option is not valid'
                })
            return Response({
                'status':'False',
                'message':serializer.errors
            })
        except Exception as e:
            print(e)
            return Response({
                'status':'False',
                'message':'somthing went wrong'
            })
class UserView(APIView):
    def get(self,request):
        try:
            id=request.GET.get('id')
            obj=User.objects.filter(id=id).first()
        
            if obj is None:
                return Response({
                    'message':'no user found'
                })
            obj1=obj.storequiz.all()
            serializer=UserSerializer(obj)
            return Response({
                'message':serializer.data
            })
        except Exception as e:
            print(e)
            return Response({
                'message':'somthing went wrong'
            })


# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.contrib.auth import authenticate
# from rest_framework import  viewsets

# from app.serializer import QuizQuestionsSerializer, QuizSerializer , CheckQuestionSerializer
# from .models import *
# from rest_framework.decorators import action


# class QuizView(APIView):

#     def get(self , request):
#         try:
#             quiz_name = request.GET.get('quiz_name')
#             if not quiz_name:
#                 return Response({
#                 'status' : False,
#                 'message' :'quiz name is required',
#                 'data' : {}
#             })
            
#             quiz_obj = Quiz.objects.filter(quiz_name__icontains= request.GET.get('quiz_name'))
#             if not quiz_obj.exists():
#                 return Response({
#                     'status' : False,
#                     'message' :'no quiz found',
#                     'data' : {}
#                 })
#             quiz_questions = quiz_obj[0].quiz_questions.all()
#             serializer = QuizQuestionsSerializer(quiz_questions , many = True)

#             return Response({
#                 'status' : True,
#                 'message' :'your quiz',
#                 'data' : serializer.data
#             })
        
#         except Exception as e:
#             print(e)

#             return Response({
#                 'status' : False,
#                 'message' :'somethign went wrong',
#                 'data' : {}
#             })



#     def post(self , request):
#         try:
#             data = request.data
#             serializer = QuizSerializer(data = data)
#             if serializer.is_valid():
#                 serializer.save()
#                 quiz_obj = Quiz.objects.get(uid = serializer.data['uid'])
#                 questions_objs = Question.objects.filter(
#                     category = quiz_obj.category)[0:quiz_obj.question_limit]

#                 for questions_obj in questions_objs:
#                     QuizQuestions.objects.create(
#                      quiz = quiz_obj,
#                      question = questions_obj
#                     )
#                 return Response({
#                     'status' : True,
#                     'message' : 'Your quiz has been created',
#                     'data' : {}
#                 })
#             return Response({
#                     'status' : False,
#                     'message' : 'you have some errors',
#                     'data' : serializer.errors
#                 })
            

                
#         except Exception as e:
#             print(e)
#             return Response({
#                 'status' : False,
#                 'message' :'somethign went wrong',
#                 'data' : {}
#             })



# class CheckQuestion(APIView):
#     def post(self , request):
#         try:
#             data = request.data

#             serializer = CheckQuestionSerializer(data = data)
#             if serializer.is_valid():
#                 answer = serializer.data['answer']
#                 question = serializer.data['question']
#                 question_obj = Question.objects.get(uid = question)

#                 if not question_obj.answer.filter(answer = answer).exists():
#                     return Response({
#                         'status' : False , 
#                         'message' : 'it seems option is not present',
#                         'data' : {}
#                     })


#                 if question_obj.answer.filter(answer = answer , is_correct = True).exists():
#                     return Response({
#                         'status' : True , 
#                         'message' : 'Hurray your answer is correct',
#                         'data' : {}
#                     })
                
#                 return Response({
#                         'status' : False , 
#                         'message' : 'no your answer is in-correct',
#                         'data' : {}
#                     })
#             return Response({
#                         'status' : False , 
#                         'message' : 'somethign went error',
#                         'data' : serializer.errors
#                     })
#         except Exception as e:
#             return Response({
#                         'status' : False , 
#                         'message' : 'no your answer is in correct',
#                         'data' : {}
#                     })