from django.contrib import admin
from .models import Todo, CompletedTodoProxy


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "completed_or_not",
        "user",
        "date_started",
        "date_completed",
    ]
    list_filter = ["is_completed"]
    readonly_fields = ["date_completed"]


@admin.register(CompletedTodoProxy)
class CompletedTodoProxyAdmin(TodoAdmin):
    ...
