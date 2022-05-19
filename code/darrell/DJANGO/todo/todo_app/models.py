from django.db import models


class TodoItem(models.Model):
    description = models.CharField(max_length=200)
    created_date = models.DateField()
    completed_date = models.DateField()
    is_completed = models.BooleanField()

    def __str__(self):
        return self.description
