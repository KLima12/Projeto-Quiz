from django.db import models
from django.contrib.auth.models import User
from quiz_admin.models import Quiz


class UserScore(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user")
    quiz = models.ForeignKey(
        Quiz, on_delete=models.CASCADE, related_name="quiz")
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}"
