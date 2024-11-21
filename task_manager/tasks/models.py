from django.db import models
from django.utils.translation import gettext_lazy as _
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=False,
                               verbose_name=_('Author'), related_name='Author')
    name = models.CharField(max_length=200, unique=True,
                            verbose_name=_('Name'), blank=False)
    description = models.TextField(verbose_name=_('Description'))
    status = models.ForeignKey(Status, on_delete=models.PROTECT, blank=False,
                               verbose_name=_('Status'))
    executor = models.ForeignKey(User, blank=True, on_delete=models.PROTECT,
                                 null=True, verbose_name=_('Executor'),
                                 related_name='Executor')
    labels = models.ManyToManyField(Label, blank=True,
                                    related_name='Labels',
                                    verbose_name=_('Labels'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
