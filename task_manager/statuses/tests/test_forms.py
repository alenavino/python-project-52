from task_manager.statuses.tests.testcase import StatusTestCase
from task_manager.statuses.forms import StatusForm


class StatusFormsTest(StatusTestCase):
    def test_status_form(self):
        form = StatusForm(data={
            'name': 'in progress',
        })
        self.assertTrue(form.is_valid())

        form = StatusForm(data={
            'name': ''
        })
        self.assertFalse(form.is_valid())
