from django.shortcuts import render
from task_manager.users.models import User
from .forms import UserForm, UserUpdateForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _


class IndexView(View):

    def get(self, request):
        users = User.objects.all()[:15]
        return render(request, 'users/index.html', context={
            'users': users,
        })


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('User is successfully registered')


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = _('User Profile is successfully changed')


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = _('User successfully deleted')
