from rest_framework import serializers
from .models import Quiz, Question


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class QuesstionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
