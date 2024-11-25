from task_manager.tasks.tests.testcase import TaskTestCase
from task_manager.tasks.models import Task


class TaskModelTest(TaskTestCase):

    def test(self):
        self.my_model = Task.objects.create(
            author=self.user1,
            name='Task 3',
            description='Description 3',
            status=self.status1,
            executor=self.user1,
        )

        self.my_model.labels.add(self.label1)

        self.assertEqual(self.my_model.author, self.user1)
        self.assertEqual(self.my_model.name, 'Task 3')
        self.assertEqual(self.my_model.description, 'Description 3')
        self.assertEqual(self.my_model.status, self.status1)
        self.assertEqual(self.my_model.executor, self.user1)
        self.assertEqual(self.my_model.labels.all()[0], self.label1)
