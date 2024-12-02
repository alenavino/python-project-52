from django.urls import reverse_lazy

from task_manager.users.tests.testcase import UserTestCase


class UserViewsTest(UserTestCase):
    def test_index(self):
        response = self.client.get(reverse_lazy("users"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/index.html")

    def test_create_user(self):
        response = self.client.get(reverse_lazy("user_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/create.html")

        response = self.client.post(
            reverse_lazy("user_create"),
            data={
                "first_name": "Garry",
                "last_name": "Potter",
                "username": "Garry",
                "password1": "ExpectoPatronum",
                "password2": "ExpectoPatronum",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_update_user(self):
        response = self.client.get(
            reverse_lazy("user_update", kwargs={"pk": self.user1.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        self.client.force_login(self.user1)
        response = self.client.get(
            reverse_lazy("user_update", kwargs={"pk": self.user1.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/update.html")

        response = self.client.post(
            reverse_lazy("user_update", kwargs={"pk": self.user1.id}),
            data={
                "first_name": "Garry",
                "last_name": "Potter",
                "username": "Garry",
                "password1": "ExpectoPatronum",
                "password2": "ExpectoPatronum",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("users"))

        self.client.force_login(self.user2)
        response = self.client.get(
            reverse_lazy("user_update", kwargs={"pk": self.user1.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("users"))

    def test_delete_user(self):
        response = self.client.get(
            reverse_lazy("user_delete", kwargs={"pk": self.user1.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        self.client.force_login(self.user2)
        response = self.client.get(
            reverse_lazy("user_delete", kwargs={"pk": self.user1.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("users"))

        self.client.force_login(self.user1)
        response = self.client.get(
            reverse_lazy("user_delete", kwargs={"pk": self.user1.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/delete.html")

        response = self.client.post(
            reverse_lazy("user_delete", kwargs={"pk": self.user1.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("users"))
