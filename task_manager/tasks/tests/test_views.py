from task_manager.tasks.tests.testcase import TaskTestCase
from django.urls import reverse_lazy


class TaskViewsTest(TaskTestCase):

    def test_index(self):
        response = self.client.get(reverse_lazy('tasks'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        self.client.force_login(self.user1)
        response = self.client.get(reverse_lazy('tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/index.html')

    def test_filter(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse_lazy('tasks'),
                                   {"status": self.status1.pk})
        self.assertEqual(response.context['tasks'].count(), 2)
        self.assertContains(response, self.task1.name)
        self.assertContains(response, self.task2.name)

        response = self.client.get(reverse_lazy('tasks'),
                                   {"executor": self.user2.pk})
        self.assertEqual(response.context['tasks'].count(), 2)
        self.assertContains(response, self.task1.name)
        self.assertContains(response, self.task2.name)

        response = self.client.get(reverse_lazy('tasks'),
                                   {"labels": self.label1.pk})
        self.assertEqual(response.context['tasks'].count(), 2)
        self.assertContains(response, self.task1.name)
        self.assertContains(response, self.task2.name)

        response = self.client.get(reverse_lazy('tasks'), {"self_tasks": "on"})
        self.assertEqual(response.context['tasks'].count(), 1)
        self.assertContains(response, self.task1.name)
        self.assertNotContains(response, self.task2.name)

    def test_create_task(self):
        response = self.client.get(reverse_lazy('task_create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        self.client.force_login(self.user1)
        response = self.client.get(reverse_lazy('task_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/create.html')

        response = self.client.post(reverse_lazy('task_create'), data={
            'name': 'Task 3',
            'description': 'Description 3',
            'status': 1,
            'executor': 1,
            'labels': 2
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))

    def test_show(self):
        response = self.client.get(reverse_lazy('task_show',
                                                kwargs={'pk': self.task1.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        self.client.force_login(self.user1)
        response = self.client.get(reverse_lazy('task_show',
                                                kwargs={'pk': self.task1.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/show.html')

    def test_update_task(self):
        response = self.client.get(reverse_lazy('task_update', kwargs={
            'pk': self.task1.pk
        }))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        self.client.force_login(self.user1)
        response = self.client.get(reverse_lazy('task_update', kwargs={
            'pk': self.task1.pk
        }))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/update.html')

        response = self.client.post(reverse_lazy('task_update', kwargs={
            'pk': self.task1.pk
        }), data={
            'name': 'Task 4',
            'description': 'Description 4',
            'status': 2,
            'executor': 2,
            'labels': 1
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))

    def test_delete_task(self):
        response = self.client.get(reverse_lazy('task_delete', kwargs={
            'pk': self.task1.pk
        }))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        self.client.force_login(self.user2)
        response = self.client.get(reverse_lazy('task_delete', kwargs={
            'pk': self.task1.pk
        }))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))

        self.client.force_login(self.user1)
        response = self.client.get(reverse_lazy('task_delete', kwargs={
            'pk': self.task1.pk
        }))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/delete.html')

        response = self.client.post(reverse_lazy('task_delete', kwargs={
            'pk': self.task1.pk
        }))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('tasks'))
