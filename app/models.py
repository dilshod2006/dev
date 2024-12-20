from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=1024)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"from {self.user.username} at {self.date}"
