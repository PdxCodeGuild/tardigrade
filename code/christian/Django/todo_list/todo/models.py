from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class TodoList(models.Model):
    title = models.TextField()

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title[:50]

class TodoItem(models.Model):
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("item-update", args=[str(self.todo_list.id), str(self.id)])

    def __str__(self):
        return f"{self.description}"

    class Meta:
        ordering = ["date_created"]