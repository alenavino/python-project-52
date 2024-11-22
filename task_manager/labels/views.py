from django.shortcuts import render, redirect
from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from .forms import LabelForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.views import View
from task_manager.mixins import Login_mixin


class IndexView(Login_mixin, View):

    def get(self, request):
        labels = Label.objects.all()
        return render(request, 'labels/index.html', context={
            'labels': labels,
        })


class LabelCreateView(Login_mixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully created')


class LabelUpdateView(Login_mixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label changed successfully')


class LabelDeleteView(SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully deleted')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, _('You are not logged in! Please sign in.')
                )
            return redirect('login')
        elif Task.objects.filter(labels=kwargs['pk']):
            messages.error(
                request, _(
                    'Cannot delete label because it is in use'
                    )
                )
            return redirect('labels')
        else:
            return super().dispatch(request, *args, **kwargs)
