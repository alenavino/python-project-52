from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models.deletion import ProtectedError


class LoginMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, _('You are not logged in! Please sign in.')
            )
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)


class AuthorPermissionMixin(UserPassesTestMixin):
    permission_denied_url = None
    redirect_field_name = None

    def test_func(self):
        return self.get_object().author == self.request.user

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result:
            messages.error(request, self.permission_denied_message)
            return redirect(self.permission_denied_url)
        return super().dispatch(request, *args, **kwargs)


class UserPermissionMixin(UserPassesTestMixin):
    permission_denied_url = None
    redirect_field_name = None

    def test_func(self):
        return self.get_object() == self.request.user

    def dispatch(self, request, *args, **kwargs):
        user_test_result = self.get_test_func()()
        if not user_test_result:
            messages.error(request, self.permission_denied_message)
            return redirect(self.permission_denied_url)
        return super().dispatch(request, *args, **kwargs)


class ProtectedErrorMixin:
    protected_error_message = ''
    permission_denied_url = None

    def post(self, request, *args, **kwargs):
        try:
            return super().post(self, request, *args, **kwargs)
        except ProtectedError:
            messages.error(
                request, self.protected_error_message
            )
            return redirect(self.permission_denied_url)
