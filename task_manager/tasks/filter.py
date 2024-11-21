import django_filters
from .models import Task
from django.forms.widgets import CheckboxInput
from django.utils.translation import gettext_lazy as _


class TaskFilter(django_filters.FilterSet):
    self_tasks = django_filters.BooleanFilter(
        widget=CheckboxInput,
        label=_('Only their own tasks'),
        method='filter_self_tasks',
    )

    def filter_self_tasks(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']