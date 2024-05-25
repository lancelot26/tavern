from .models import Task, Comment
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','content','reward', 'banner']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']