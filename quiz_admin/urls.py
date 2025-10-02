from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
app_name = 'quiz_admin'
urlpatterns = [
    path('registration/login/', LoginView.as_view(template_name='quiz_admin/login.html', name='login')),
    path('', views.QuizListApiView.as_view(), name="api-view"),
    path('create-quiz/', views.create_quiz, name="create-quiz"),
]
