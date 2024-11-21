from task_manager.tasks.tests.testcase import TaskTestCase
from task_manager.tasks.forms import TaskForm


class TaskFormsTest(TaskTestCase):
    def test_task_form(self):
        form = TaskForm(data={
            'name': 'Task 3',
            'description': 'Description 3',
            'status': 1,
            'executor': 1,
            'labels': 1
        })
        self.assertTrue(form.is_valid())

        form = TaskForm(data={
            'name': 'Task 3',
            'description': '',
            'status': 1,
            'executor': 1,
            'labels': 1
        })
        self.assertFalse(form.is_valid())

        form = TaskForm(data={
            'name': '',
            'description': 'Description 3',
            'status': 1,
            'executor': 1,
            'labels': 1
        })
        self.assertFalse(form.is_valid())
