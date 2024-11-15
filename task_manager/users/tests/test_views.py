from task_manager.users.tests.testcase import UserTestCase
from django.urls import reverse_lazy


class UserViewsTest(UserTestCase):

    def test_index(self):
        response = self.client.get(reverse_lazy('users'))
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        response = self.client.get(reverse_lazy('user_create'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse_lazy('user_create'), data={
            'first_name': 'Garry',
            'last_name': 'Potter',
            'username': 'Garry',
            'password': 'ExpectoPatronum'
        })
        self.assertEqual(response.status_code, 302)
