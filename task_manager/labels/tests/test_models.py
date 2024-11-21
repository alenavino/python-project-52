from task_manager.labels.tests.testcase import LabelTestCase
from task_manager.labels.models import Label


class LabelModelTest(LabelTestCase):

    def test(self):
        self.my_model = Label.objects.create(
            name='new_label')

        self.assertEqual(self.my_model.name, 'new_label')
