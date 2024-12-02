from django.shortcuts import redirect
from task_manager.labels.models import Label
from task_manager.tasks.models import Task
from .forms import LabelForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from task_manager.mixins import LoginMixin


class IndexView(LoginMixin, ListView):
    model = Label
    template_name = "labels/index.html"
    context_object_name = "labels"


class LabelCreateView(LoginMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = "labels/create.html"
    success_url = reverse_lazy("labels")
    success_message = _("Label successfully created")


class LabelUpdateView(LoginMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = "labels/update.html"
    success_url = reverse_lazy("labels")
    success_message = _("Label changed successfully")


class LabelDeleteView(LoginMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = "labels/delete.html"
    success_url = reverse_lazy("labels")
    success_message = _("Label successfully deleted")

    def post(self, request, *args, **kwargs):
        if Task.objects.filter(labels=kwargs["pk"]):
            messages.error(request, _("Cannot delete label because it is in use"))
            return redirect("labels")
        return super().post(request, *args, **kwargs)
