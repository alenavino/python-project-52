from django.shortcuts import render, redirect
from task_manager.statuses.models import Status
from .forms import StatusForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.db.models.deletion import ProtectedError
from task_manager.mixins import Login_mixin


class IndexView(Login_mixin, View):

    def get(self, request):
        statuses = Status.objects.all()
        return render(request, 'statuses/index.html', context={
            'statuses': statuses,
        })


class StatusCreateView(Login_mixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully created')


class StatusUpdateView(Login_mixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status changed successfully')


class StatusDeleteView(SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status successfully deleted')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, _('You are not logged in! Please sign in.')
                )
            return redirect('login')
        try:
            return super().dispatch(request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request, _(
                    'Cannot delete status because it is in use'
                    )
                )
            return redirect('statuses')
