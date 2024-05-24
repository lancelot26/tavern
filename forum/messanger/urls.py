from django.urls import path
from . import views

app_name = 'messanger'

urlpatterns = [
    path('<int:pk>/update_message/', views.UpdateMessage.as_view(), name='update_message'),
    path('<int:pk>/delete_message/', views.DeleteMessage.as_view(), name='delete_message'),
]