from task_manager.users.tests.testcase import UserTestCase
from task_manager.users.models import User


class UserModelTest(UserTestCase):

    def test(self):
        self.my_model = User.objects.create(
            first_name='Hermione',
            last_name='Granger',
            username='Jeen',
            password='Alohomora')

        self.assertEqual(self.my_model.first_name, 'Hermione')
        self.assertEqual(self.my_model.last_name, 'Granger')
        self.assertEqual(self.my_model.username, 'Jeen')
        self.assertEqual(self.my_model.password, 'Alohomora')
