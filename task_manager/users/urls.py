from django.urls import path
from task_manager.users.views import IndexView, UserCreateView


urlpatterns = [
    path('', IndexView.as_view(), name='users'),
    path('create/', UserCreateView.as_view(), name='user_create'),
]
