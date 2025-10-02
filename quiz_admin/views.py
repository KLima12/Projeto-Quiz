from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Quiz
from .serializes import QuizSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class QuizListApiView(generics.ListCreateAPIView):
    """
    Api View para listar todos os quizes e criar novas opções de quiz;
    """
    permission_classes = (IsAuthenticated,)
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_permissions(self):
        """
        Permissões por método: GET público, POST só autenticado.
        """
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return [AllowAny()]


@login_required(login_url='/accounts/login/')
def create_quiz(request):
    if request.method == "POST":
        text = request.POST.get('text')
        description = request.POST.get('description')
        if text:
            Quiz.objects.create(text=text, description=description)
            messages.success(request, "Quiz criado com sucesso!")

        else:
            messages.error(request, "Texto é obrigatorio")
    return render(request, 'create_quiz/create_quiz.html')
