from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .serializes import QuizSerializer
from .models import Quiz, Question, AnswerChoice, UserScore


# @api_view(['GET'])
# def home(request):
#     all_quiz = Quiz.objects.all()
#     serializer = QuizSerializer(all_quiz, many=True)
#     return Response(serializer.data)

def login(request):
    if request.method == "POST":
        pass


def home(request):
    quiz = Quiz.objects.all()
    return render(request, "home/home.html", context={'quiz': quiz})


def question(request, id):
    """Usuario manda o id pra minha question, eu vou filtrar no meu bd question todos textos que tenha essa question"""
    """Esse question ele procura as questõe relacionadas ao quiz"""
    question = Question.objects.filter(quiz=id)

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
        print(f" score final: {score}")

    return render(request, 'question/question.html', context={'question': question})
