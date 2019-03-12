# Django
from django.contrib import admin

# local Django
from task.models import Task


class AdminTask(admin.ModelAdmin):
    """
    Admin-Task
    """

    list_display = ('title', 'description')
    search_fields = ('title',)


admin.site.register(Task, AdminTask)
