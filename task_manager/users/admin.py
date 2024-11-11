from django.contrib import admin
from .models import User
from django.contrib.admin import DateFieldListFilter


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name')
    search_fields = ['username', 'full_name']
    list_filter = (('created_at', DateFieldListFilter),)
