from django.shortcuts import render
from rest_framework import generics
from .models import Quiz
# Para enviar o token
from django.contrib.auth.views import LoginView
from .serializes import QuizSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


class CustomLoginView(LoginView): 
    template_name = 'accounts/login.html' 
    

class QuizListApiView(generics.ListCreateAPIView):
    """
    Api View para listar todos os quizes e criar novas opções de quiz;
    """
    permission_classes = (IsAuthenticated,)
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

@login_required
def create_quiz(request):
    if request.method == "POST":
        quiz = request.POST.get('quiz')
        descricao = request.POST.get('descricao')
    return render(request, 'create_quiz/create_quiz.html')
