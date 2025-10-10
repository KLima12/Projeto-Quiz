from django.shortcuts import render, redirect, get_object_or_404
from .models import Quiz
from rest_framework import generics
from .serializes import QuizSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name="dispatch")
class QuizListCreateApiView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    # Somente POST é protegido aqui
    # Se quisesse proteger ambos, usaria: permission_classes = (IsAuthenticated,)
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]

        return [AllowAny()]


class QuizDetailUpdateDestroyApiView(generics.RetrieveDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (IsAuthenticated,)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('create-quiz')
        else:
            messages.error(request, 'email ou senha incorretos!')
    return render(request, 'registration/login.html', {'next': request.GET.get('next', '')})


@login_required
def create_quiz(request):
    # if request.method == "POST":
    #     text = request.POST.get('text').strip()
    #     description = request.POST.get('description').strip()
    #     if text:
    #         Quiz.objects.create(text=text, description=description)
    #         messages.success(request, "Quiz criado com sucesso!")
    #         # Usando redirect, pois sem o redirect quando atualiza a página o django não fica enviando dados anteriores.
    #         return redirect('create-quiz')

    #     else:
    #         messages.error(request, "Texto é obrigatorio")
    return render(request, 'create_quiz/create_quiz.html')
