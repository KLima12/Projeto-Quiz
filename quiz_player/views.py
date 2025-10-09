from django.shortcuts import render, redirect
from quiz_admin.models import Quiz, Question, AnswerChoice
from .models import UserScore
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # Aplica o hash de senha
            User.objects.create_user(username=username, password=password)

            return redirect('login')
    else:
        form = RegisterUserForm()

    return render(request, 'registration/register.html', context={'form': form})


@login_required
def home(request):
    quiz = Quiz.objects.all()
    return render(request, "home/home.html", context={'quiz': quiz})


@login_required
def question(request, id):
    question = Question.objects.filter(quiz=id)
    quiz = Quiz.objects.get(id=id)

    if request.method == "POST":
        score = 0
        # Retorna um dicionario com todos os dados
        for nome_campo, id_da_resposta in request.POST.items():
            # Aqui fiz assim por causa que sem isso, o formulario me daria o id do form e csrf token em vez dos campos que realmente quero
            if nome_campo.startswith('opcoes'):
                # Nome_campo = opcoes1, opcoes3, id = 1, 8
                answer = AnswerChoice.objects.get(id=id_da_resposta)
                if answer.is_correct:
                    score += 1

        user_score, created = UserScore.objects.get_or_create(
            user=request.user,
            quiz=quiz,
            defaults={'score': score},
        )

        if not created:
            user_score.score = score
            user_score.save()

    return render(request, 'question/question.html', context={'question': question})
