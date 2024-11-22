from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class LoginMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, _('You are not logged in! Please sign in.')
                )
            return redirect(reverse_lazy('login'))
        return super().dispatch(request, *args, **kwargs)
