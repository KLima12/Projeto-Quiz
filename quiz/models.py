from django.db import models
from django.contrib.auth.models import User


# Ex: Quiz de historia e a descrição
# A tabela quiz cria uma nova linha com as informações + id unico.


class Quiz(models.Model):
    text = models.CharField(max_length=2200)
    desciption = models.TextField()

    def __str__(self):
        return self.text

# Qual é a capital do Brasil. Você diz que essa question pertence ao Quiz de id=1


class Question(models.Model):
    text = models.CharField(max_length=255)
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="question")

    def __str__(self):
        return self.text

# Para cada Question, adiciono opções de respostas. Is_correct = True para resposta correta e False para as outras.


class AnswerChoice(models.Model):
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answer")

    def __str__(self):
        return f"Opção para: {self.question.text}"


class UserScore(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user")
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="quiz")
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}"
