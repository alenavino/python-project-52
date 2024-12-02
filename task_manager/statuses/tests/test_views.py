from task_manager.statuses.tests.testcase import StatusTestCase
from django.urls import reverse_lazy


class StatusViewsTest(StatusTestCase):
    def test_index(self):
        response = self.client.get(reverse_lazy("statuses"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        self.client.force_login(self.user1)
        response = self.client.get(reverse_lazy("statuses"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "statuses/index.html")

    def test_create_status(self):
        response = self.client.get(reverse_lazy("status_create"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        self.client.force_login(self.user1)
        response = self.client.get(reverse_lazy("status_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "statuses/create.html")

        response = self.client.post(
            reverse_lazy("status_create"), data={"name": "deleted"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("statuses"))

    def test_update_status(self):
        response = self.client.get(
            reverse_lazy("status_update", kwargs={"pk": self.status1.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        self.client.force_login(self.user1)
        response = self.client.get(
            reverse_lazy("status_update", kwargs={"pk": self.status1.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "statuses/update.html")

        response = self.client.post(
            reverse_lazy("status_update", kwargs={"pk": self.status1.id}),
            data={"name": "restored"},
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("statuses"))

    def test_delete_status(self):
        response = self.client.get(
            reverse_lazy("status_delete", kwargs={"pk": self.status2.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        self.client.force_login(self.user1)
        response = self.client.get(
            reverse_lazy("status_delete", kwargs={"pk": self.status2.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "statuses/delete.html")

        response = self.client.post(
            reverse_lazy("status_delete", kwargs={"pk": self.status2.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("statuses"))
