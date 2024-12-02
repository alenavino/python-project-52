from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import CreateView, DeleteView, UpdateView
from django_filters.views import FilterView

from task_manager.mixins import LoginMixin, UserPermissionMixin
from task_manager.tasks.models import Task

from .filter import TaskFilter
from .forms import TaskForm


class IndexView(LoginMixin, FilterView):
    model = Task
    filterset_class = TaskFilter
    template_name = "tasks/index.html"
    context_object_name = "tasks"


class TaskCreateView(LoginMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/create.html"
    success_url = reverse_lazy("tasks")
    success_message = _("Task successfully created")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskView(LoginMixin, View):
    def get(self, request, **kwargs):
        task = get_object_or_404(Task, id=kwargs["pk"])
        labels = list(Task.objects.get(id=kwargs["pk"]).labels.all())
        return render(
            request, "tasks/show.html", context={"task": task, "labels": labels}
        )


class TaskUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/update.html"
    success_url = reverse_lazy("tasks")
    success_message = _("Task changed successfully")


class TaskDeleteView(
    LoginMixin, UserPermissionMixin, SuccessMessageMixin, DeleteView
):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy("tasks")
    success_message = _("Task successfully deleted")
    permission_denied_message = _("A task can only be deleted by its author.")
    permission_denied_url = reverse_lazy("tasks")

    def test_func(self):
        return self.get_object().author == self.request.user
