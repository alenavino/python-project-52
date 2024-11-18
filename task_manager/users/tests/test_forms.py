from task_manager.users.tests.testcase import UserTestCase
from task_manager.users.forms import UserForm, UserUpdateForm


class UserFormsTest(UserTestCase):
    def test_user_form(self):
        form = UserForm(data={
            'first_name': 'Garry',
            'last_name': 'Potter',
            'username': 'Garry',
            'password1': 'ExpectoPatronum',
            'password2': 'ExpectoPatronum'
        })
        self.assertTrue(form.is_valid())

        form = UserForm(data={
            'first_name': 'Garry',
            'last_name': 'Potter',
            'username': 'Garry',
            'password1': 'ExpectoPatronum',
            'password2': 'PatronumExpecto'
        })
        self.assertFalse(form.is_valid())

        form = UserForm(data={
            'first_name': 'Garry',
            'last_name': 'Potter',
            'username': 'Garry',
            'password1': 'E',
            'password2': 'E'
        })
        self.assertFalse(form.is_valid())

        form = UserForm(data={
            'first_name': 'Garry',
            'last_name': 'Potter',
            'username': 'Garry',
            'password1': 'ExpectoPatronum',
        })
        self.assertFalse(form.is_valid())

        form = UserForm(data={
            'first_name': 'Garry',
            'last_name': 'Potter',
            'password1': 'ExpectoPatronum',
            'password2': 'ExpectoPatronum'
        })
        self.assertFalse(form.is_valid())

    def test_user_update_form(self):
        form = UserUpdateForm(data={
            'first_name': 'Garry',
            'last_name': 'Potter',
            'username': 'Garry',
            'password1': 'ExpectoPatronum',
            'password2': 'ExpectoPatronum'
        })
        self.assertTrue(form.is_valid())

        form = UserUpdateForm(data={
            'first_name': 'Garry',
            'last_name': 'Potter',
            'username': 'Garry',
            'password1': 'ExpectoPatronum',
            'password2': 'PatronumExpecto'
        })
        self.assertFalse(form.is_valid())

        form = UserUpdateForm(data={
            'first_name': 'Garry',
            'last_name': 'Potter',
            'username': 'Garry',
            'password1': 'E',
            'password2': 'E'
        })
        self.assertFalse(form.is_valid())

        form = UserUpdateForm(data={
            'first_name': 'Garry',
            'last_name': 'Potter',
            'username': 'Garry',
            'password1': 'ExpectoPatronum',
        })
        self.assertFalse(form.is_valid())

        form = UserUpdateForm(data={
            'first_name': 'Garry',
            'last_name': 'Potter',
            'password1': 'ExpectoPatronum',
            'password2': 'ExpectoPatronum'
        })
        self.assertFalse(form.is_valid())
