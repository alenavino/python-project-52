from django.test import TestCase, Client
from task_manager.statuses.models import Status


class StatusTestCase(TestCase):
    fixtures = ['test_status.json']

    def setUp(self):
        self.client = Client()

        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)
        self.statuses = Status.objects.all()
        self.count = Status.objects.count()
