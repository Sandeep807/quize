from django.contrib import admin
from django.urls import path
from .views import *

from django.urls import path
from .views import *
urlpatterns = [
     path('quiz/',QuizRedyView.as_view()),
     path('user/',UserView.as_view()),
     
]

# urlpatterns = [
#     path('create-quiz/' , QuizView.as_view()),
#     path('check/' , CheckQuestion.as_view())
# ]
