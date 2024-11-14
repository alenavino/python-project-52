from django.test import TestCase
from task_manager.users.models import User


class UserModelTest(TestCase):

    def setUp(self):
        self.my_model = User.objects.create(
            first_name='a',
            last_name='b',
            username='c',
            password='abcd1234')

    def test_model(self):
        self.assertEqual(self.my_model.first_name, 'a')
        self.assertEqual(self.my_model.last_name, 'b')
        self.assertEqual(self.my_model.username, 'c')
        self.assertEqual(self.my_model.password, 'abcd1234')
