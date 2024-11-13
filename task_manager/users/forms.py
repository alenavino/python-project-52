from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'password1', 'password2'
            ]


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name'
            ]
