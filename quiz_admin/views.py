from django.shortcuts import render
from rest_framework import generics
from .models import Quiz
from .serializes import QuizSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required


class QuizListApiView(generics.ListCreateAPIView):
    """
    Api View para listar todos os quizes e criar novas opções de quiz;
    """
    permission_classes = (IsAuthenticated,)
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


@login_required
def create_quiz(request):
    return render(request, 'create_quiz/create_quiz.html')
