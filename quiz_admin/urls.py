from django.urls import path
from . import views
urlpatterns = [
    path('', views.QuizListApiView.as_view(), name="api-view"),
    path('create-quiz/', views.create_quiz, name="create-quiz"),
]
