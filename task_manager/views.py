from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse


def index(request):
    return render(request, 'index.html')


class UserLoginView(LoginView):
    template_name = 'login.html'


class UserLogoutView(LogoutView):
    pass