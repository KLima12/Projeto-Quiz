from django.contrib import admin
from .models import Quiz, Question, AnswerChoice, UserScore


class AnswerChoiceInline(admin.TabularInline):
    model = AnswerChoice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):

    list_display = ('text', 'quiz')
    inlines = [AnswerChoiceInline]


#
admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserScore)
