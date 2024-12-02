from task_manager.labels.models import Label
from task_manager.labels.tests.testcase import LabelTestCase


class LabelModelTest(LabelTestCase):
    def test(self):
        self.my_model = Label.objects.create(name="label")

        self.assertEqual(self.my_model.name, "label")
