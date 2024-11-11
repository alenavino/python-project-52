from django.shortcuts import render, redirect
from django.views import View
from task_manager.users.models import User
from .forms import UserForm
from django.urls import reverse


class IndexView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()[:15]
        return render(request, 'users/index.html', context={
            'users': users,
        })


class UserCreateView(View):

    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        return render(request, 'users/create.html', {'form': form})
