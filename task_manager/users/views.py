from task_manager.users.models import User
from .forms import UserForm, UserUpdateForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from task_manager.mixins import LoginMixin, UserPermissionMixin, ProtectedErrorMixin


class IndexView(ListView):
    model = User
    template_name = "users/index.html"
    context_object_name = "users"


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = "users/create.html"
    success_url = reverse_lazy("login")
    success_message = _("User is successfully registered")


class UserUpdateView(LoginMixin, UserPermissionMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "users/update.html"
    success_url = reverse_lazy("users")
    success_message = _("User Profile is successfully changed")
    permission_denied_message = _("You do not have permission to modify another user.")
    permission_denied_url = reverse_lazy("users")


class UserDeleteView(
    LoginMixin,
    UserPermissionMixin,
    ProtectedErrorMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy("users")
    success_message = _("User successfully deleted")
    permission_denied_message = _("You do not have permission to modify another user.")
    permission_denied_url = reverse_lazy("users")
    protected_error_message = _("Cannot delete user because it is in use")
