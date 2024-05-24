from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Messanger
from .forms import MessageForm, MessageUpdateForm
from django.views.generic import UpdateView, DeleteView


class DeleteMessage(DeleteView):
    model = Messanger
    success_url = "/communication/"
    template_name = 'messanger/delete_message.html'

class UpdateMessage(UpdateView):
    model = Messanger
    template_name = 'messanger/update_message.html'
    form_class = MessageUpdateForm

    def get_initial(self):
        return {'update_status':'(updated)'}

#def update_message(request, pk):
#    error = ''
#    if request.method == 'POST':
#        form = MessageForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('main/communication')
#        mess = Messanger.objects.get(id=pk)
#        mess.update_status = 'updated'
#        mess.save(update_fields=['update_status'])
#        form = MessageForm()
#        return render(request, 'main/communication.html', {"form":form})