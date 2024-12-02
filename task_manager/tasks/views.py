from django.shortcuts import render, get_object_or_404
from task_manager.tasks.models import Task
from .forms import TaskForm
from .filter import TaskFilter
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views import View
from task_manager.mixins import LoginMixin, AuthorPermissionMixin


class IndexView(LoginMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'


class TaskCreateView(LoginMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task successfully created')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskView(LoginMixin, View):

    def get(self, request, **kwargs):
        task = get_object_or_404(Task, id=kwargs['pk'])
        labels = list(Task.objects.get(id=kwargs['pk']).labels.all())
        return render(request, 'tasks/show.html', context={
            'task': task, 'labels': labels
        })


class TaskUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task changed successfully')


class TaskDeleteView(LoginMixin, AuthorPermissionMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _("Task successfully deleted")
    permission_denied_message = _('A task can only be deleted by its author.')
    permission_denied_url = reverse_lazy('tasks')
