from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
    path('', views.QuizListApiView.as_view(), name="api-view"),
    path('login/', views.login_user, name='login_user'),
    path('create-quiz/', views.create_quiz, name="create-quiz"),
    path('logout/', LogoutView.as_view(next_page='api-view'), name='logout'),
]
