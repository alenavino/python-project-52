from django.test import TestCase, Client
from task_manager.tasks.models import Task
from task_manager.users.models import User
from task_manager.statuses.models import Status
from task_manager.labels.models import Label


class TaskTestCase(TestCase):
    fixtures = [
        "test_user.json",
        "test_status.json",
        "test_label.json",
        "test_task.json",
    ]

    def setUp(self):
        self.client = Client()

        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)
        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.tasks = Task.objects.all()
        self.count = Task.objects.count()
