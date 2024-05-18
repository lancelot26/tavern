from django.urls import path, include
from . import views

app_name='users'

urlpatterns = [
    path('reg_form/', views.reg_form, name='reg_form'),
    path('login_form/', views.login_form, name='login_form'),
    path('logout_form/', views.logout_form, name='logout_form'),
]