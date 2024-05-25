from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    reward = models.CharField(default='1 gold coin')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    banner = models.ImageField(default='fallback.png', blank=True)
    author_name = models.CharField(max_length=150, default='')
    updated_task = models.CharField(max_length=9, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/tasks/{self.id}'

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content