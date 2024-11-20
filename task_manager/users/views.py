from django.shortcuts import render, redirect
from task_manager.users.models import User
from .forms import UserForm, UserUpdateForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.db.models.deletion import ProtectedError


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

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, _('You are not logged in! Please sign in.')
                )
            return redirect('login')
        elif request.user.pk != self.get_object().pk:
            messages.error(
                request, _(
                    'You do not have permission to modify another user.'
                    )
                )
            return redirect('users')
        return super().dispatch(request, *args, **kwargs)


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = _('User successfully deleted')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, _('You are not logged in! Please sign in.')
                )
            return redirect('login')
        elif request.user.pk != self.get_object().pk:
            messages.error(
                request, _(
                    'You do not have permission to modify another user.'
                    )
                )
            return redirect('users')
        try:
            return super().dispatch(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request, _(
                    'Cannot delete user because it is in use'
                    )
                )
            return redirect('users')
