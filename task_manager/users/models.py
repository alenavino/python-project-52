from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
