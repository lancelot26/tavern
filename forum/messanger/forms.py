from .models import Messanger
from django.forms import ModelForm

class MessageForm(ModelForm):
    class Meta:
        model = Messanger
        fields = ['content']