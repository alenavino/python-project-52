from django.test import Client, TestCase

from task_manager.users.models import User


class UserTestCase(TestCase):
    fixtures = ["test_user.json"]

    def setUp(self):
        self.client = Client()

        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.users = User.objects.all()
        self.count = User.objects.count()
