from django.contrib import admin

from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'priority', 'status')
    list_filter = ('priority', 'status')
    search_fields = ('title', 'description')


admin.site.register(Task)

