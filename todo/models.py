from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="", blank=True)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_started = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

    @property
    def completed_or_not(self):
        """
        property method used in admin panel
        returns completed if is_completed is True else returns Not Completed
        """
        return "Completed" if self.is_completed else "Not Completed"

    def _update_date_completed(self):
        """
        helper method to set date_completed to the current datetime if is_completed is True
        else set date_completed to None
        """
        if self.is_completed is True and self.date_completed is None:
            self.date_completed = timezone.now()
        elif self.is_completed is not True and self.date_completed is not None:
            self.date_completed = None

    def save(self, *args, **kwargs):
        self._update_date_completed()
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["id"]


class CompletedTodoProxy(Todo):
    """
    Proxy that returns all the completed todos.
    """

    class CompletedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(is_completed=True)

    objects = CompletedManager()

    class Meta:
        proxy = True
        verbose_name = "Completed Todo"
        verbose_name_plural = "Completed Todos"
