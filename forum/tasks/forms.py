from .models import Task, Comment
from django.forms import ModelForm

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','content','reward', 'banner']

class UpdateTaskForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['updated_task'].disabled = True
    class Meta:
        model = Task
        fields = ['title','content','reward', 'banner', 'updated_task']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']