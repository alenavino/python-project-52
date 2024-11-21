from task_manager.labels.tests.testcase import LabelTestCase
from task_manager.labels.forms import LabelForm


class LabelFormsTest(LabelTestCase):
    def test_label_form(self):
        form = LabelForm(data={
            'name': 'label1',
        })
        self.assertTrue(form.is_valid())

        form = LabelForm(data={
            'name': ''
        })
        self.assertFalse(form.is_valid())
