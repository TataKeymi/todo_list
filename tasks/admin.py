from django.contrib import admin

from tasks.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ["content",]
    list_display = ["content", "created_at", "deadline", "is_done", ]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name", ]
