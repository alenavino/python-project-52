from django.urls import path

from task_manager.tasks.views import (
    IndexView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    TaskView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="tasks"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/", TaskView.as_view(), name="task_show"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
]
