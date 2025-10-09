from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Quiz
from .serializes import QuizSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test


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


class TaskDetailApiView(generics.RetrieveUpdateAPIView):
    """
    API View para buscar editar e deletar
    """
    permission_classes = (IsAuthenticated,)
    queryset = Quiz.objects.all()
    lookup_field = 'id'


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        print(f"{username} AQUIs")
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
