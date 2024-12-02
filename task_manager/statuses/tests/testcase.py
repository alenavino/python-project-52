from django.test import Client, TestCase

from task_manager.statuses.models import Status
from task_manager.users.models import User


class StatusTestCase(TestCase):
    fixtures = ["test_user.json", "test_status.json"]

    def setUp(self):
        self.client = Client()

        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.statuses = Status.objects.all()
        self.count = Status.objects.count()
