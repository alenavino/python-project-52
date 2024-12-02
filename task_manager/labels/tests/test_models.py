from task_manager.labels.tests.testcase import LabelTestCase
from task_manager.labels.models import Label


class LabelModelTest(LabelTestCase):
    def test(self):
        self.my_model = Label.objects.create(name="label")

        self.assertEqual(self.my_model.name, "label")
