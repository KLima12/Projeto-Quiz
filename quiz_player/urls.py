from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('home/', views.home, name="home"),
    path('question/<int:id>/', views.question, name="question"),
]
