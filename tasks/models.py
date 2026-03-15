from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)
        verbose_name = "tag"
        verbose_name_plural = "tags"

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ("is_done",)
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return self.content

