from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # Связь с моделью пользователя
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    total_tests = models.PositiveIntegerField(default=0)
    total_time = models.FloatField(default=0.0)
    record_speed = models.FloatField(default=0.0)
    
    def __str__(self):
        return f"Профиль пользователя {self.user.username}"
    

class TestResult(models.Model):
    # Связь с моделью UserProfile
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    speed = models.FloatField()
    accuracy = models.FloatField()
    time_taken = models.FloatField()
    test_date = models.DateTimeField()

    def rounded_time_taken(self):
        return round(self.time_taken, 1)

    def __str__(self):
        return f"Результаты теста для {self.user_profile.user.username}"


