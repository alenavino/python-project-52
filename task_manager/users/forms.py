from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import User


class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["first_name",
                  "last_name",
                  "username",
                  "password1",
                  "password2"]


class UserUpdateForm(UserForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["first_name",
                  "last_name",
                  "username",
                  "password1",
                  "password2"]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():  # noqa
            raise forms.ValidationError(_("Username already exists."))
        return username
