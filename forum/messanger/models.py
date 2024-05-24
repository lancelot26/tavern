from django.db import models
from django.contrib.auth.models import User

class Messanger(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content