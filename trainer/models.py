from django.db import models
from django.contrib.auth.models import User


class TypingTestText(models.Model):
    text = models.TextField('Введите текст для тестирования')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Текст {self.id} ({self.created_at.strftime('%Y-%m-%d %H:%M:%S')})"

