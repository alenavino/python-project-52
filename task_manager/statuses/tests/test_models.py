from task_manager.statuses.models import Status
from task_manager.statuses.tests.testcase import StatusTestCase


class StatusModelTest(StatusTestCase):
    def test(self):
        self.my_model = Status.objects.create(name="testing")

        self.assertEqual(self.my_model.name, "testing")
