from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


def index(request):
    return render(request, 'index.html')


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    success_message = _('You are logged in')


class UserLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
