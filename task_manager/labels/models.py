from django.db import models
from django.utils.translation import gettext_lazy as _


class Label(models.Model):
    name = models.CharField(max_length=200, unique=True,
                            verbose_name=_('Name'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
