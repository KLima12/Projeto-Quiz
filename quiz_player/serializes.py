from rest_framework import serializers
from .models import Quiz, AnswerChoice, Question, UserScore


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
