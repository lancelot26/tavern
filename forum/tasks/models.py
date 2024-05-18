from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    reward = models.CharField(default='1 gold coin')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    banner = models.ImageField(default='fallback.png', blank=False, upload_to='media')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/tasks/{self.id}'