from task_manager.labels.tests.testcase import LabelTestCase
from django.urls import reverse_lazy


class LabelViewsTest(LabelTestCase):

    def test_index(self):
        response = self.client.get(reverse_lazy('labels'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        self.client.force_login(self.user1)
        response = self.client.get(reverse_lazy('labels'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/index.html')

    def test_create_label(self):
        response = self.client.get(reverse_lazy('label_create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        self.client.force_login(self.user1)
        response = self.client.get(reverse_lazy('label_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/create.html')

        response = self.client.post(reverse_lazy('label_create'), data={
            'name': 'label 5'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels'))

    def test_update_label(self):
        response = self.client.get(reverse_lazy('label_update', kwargs={
            'pk': self.label1.id
            }))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        self.client.force_login(self.user1)
        response = self.client.get(reverse_lazy('label_update', kwargs={
            'pk': self.label1.id
            }))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/update.html')

        response = self.client.post(reverse_lazy('label_update', kwargs={
            'pk': self.label1.id
            }), data={
            'name': 'label 6'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels'))

    def test_delete_label(self):
        response = self.client.get(reverse_lazy('label_delete', kwargs={
            'pk': self.label1.id
            }))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        self.client.force_login(self.user1)
        response = self.client.get(reverse_lazy('label_delete', kwargs={
            'pk': self.label1.id
            }))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels'))

        response = self.client.get(reverse_lazy('label_delete', kwargs={
            'pk': self.label2.id
            }))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'labels/delete.html')

        response = self.client.post(reverse_lazy('label_delete', kwargs={
            'pk': self.label2.id
            }))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('labels'))
