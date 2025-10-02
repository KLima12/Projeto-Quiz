from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('registration/login',
         LoginView.as_view(template_name='quiz_player/login.html'), name='login'),
    path('register/', views.register_user, name='register_user'),
    path('home/', views.home, name="home"),
    path('question/<int:id>/', views.question, name="question"),
]
