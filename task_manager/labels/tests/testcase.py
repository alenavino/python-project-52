from django.test import TestCase, Client
from task_manager.labels.models import Label
from task_manager.users.models import User
from task_manager.tasks.models import Task


class LabelTestCase(TestCase):
    fixtures = ['test_user.json',
                'test_task.json',
                'test_label.json',
                'test_status.json']

    def setUp(self):
        self.client = Client()

        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)
        self.labels = Label.objects.all()
        self.count = Label.objects.count()
