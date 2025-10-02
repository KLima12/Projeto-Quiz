from django.urls import path
from .views import CustomLoginView
app_name = 'accounts'  # Para evitar conflitos
urlPatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
]
