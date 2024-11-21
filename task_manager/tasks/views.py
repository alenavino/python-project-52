from django.shortcuts import render, redirect, get_object_or_404
from task_manager.tasks.models import Task
from .forms import TaskForm
from .filter import TaskFilter
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.views import View


class IndexView(FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    ordering = 'id'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, _('You are not logged in! Please sign in.')
                )
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class TaskCreateView(SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully created')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, _('You are not logged in! Please sign in.')
                )
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class TaskView(View):

    def get(self, request, **kwargs):
        task = get_object_or_404(Task, id=kwargs['pk'])
        labels = list(Task.objects.get(id=kwargs['pk']).labels.all())
        return render(request, 'tasks/show.html', context={
            'task': task, 'labels': labels
        })

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, _('You are not logged in! Please sign in.')
                )
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class TaskUpdateView(SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task changed successfully')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, _('You are not logged in! Please sign in.')
                )
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)


class TaskDeleteView(SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully deleted')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, _('You are not logged in! Please sign in.')
                )
            return redirect('login')
        elif request.user != self.get_object().author:
            messages.error(
                request, _('A task can only be deleted by its author.')
                )
            return redirect('tasks')
        return super().dispatch(request, *args, **kwargs)
