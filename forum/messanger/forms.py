from .models import Messanger
from django.forms import ModelForm

class MessageForm(ModelForm):
    class Meta:
        model = Messanger
        fields = ['content']
class MessageUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['update_status'].disabled = True
    class Meta:
        model = Messanger
        fields = ['content', 'update_status']